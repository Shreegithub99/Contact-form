
from flask import Flask, render_template, request
import pymysql
from flaskext.mysql import MySQL


app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'agriculture'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contactform():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    if request.method=='POST': 
        email=request.form['email'] 
        name=request.form['name']
        phone=request.form['phone']
        message=request.form['message']
        
        cursor.execute('insert into contactform(email, name, phone, message) values (%s,%s,%s,%s)',(email,name,phone,message))
        conn.commit()   
       
    return render_template('index.html')

"""to show data"""

@app.route('/contactreq')
def contactrq():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    cursor.execute('select * from contactform')
    shree = cursor.fetchall()
    return render_template('contactreq.html',shree = shree)

"""to update data"""

@app.route('/conupdate',methods = ['POST'])
def contactupdate():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    if request.method == 'POST':
       email= request.form['email']
       name= request.form['name']
       phone= request.form['phone']
       message= request.form['message']
       cursor.execute('update contactform set name = %s,email = %s, phone= %s, message= %s where id=%s',(name,email,phone,message))    
       conn.commit()
       return 'Updated Succesfully'
       
       
        
if __name__ =='__main__':
    app.run(debug=True,port=7008)