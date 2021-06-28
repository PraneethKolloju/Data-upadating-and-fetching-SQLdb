from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
import yaml

app=Flask(__name__)
 
db=yaml.load(open('db.yaml'))

app.config['MYSQL_HOST']=db['mysql_host']
app.config['MYSQL_USER']=db['mysql_user']
app.config['MYSQL_PASSWORD']=db['mysql_password']
app.config['MYSQL_DB']=db['mysql_db']


mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/forcurrent',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        userDetails =request.form
        boardID=userDetails['Id']
        temp=userDetails['temp']
        cur =mysql.connection.cursor()
        cur.execute(f"INSERT INTO curnttemp(boardID,temp) VALUES({boardID},{temp})")
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    return render_template('index.html')

@app.route('/forset',methods=['GET','POST'])
def index1():
    if request.method == 'POST':
        userDetails1 =request.form
        boardID=userDetails1['bId']
        userID=userDetails1['uId']
        temp=userDetails1['temp1']
        cur =mysql.connection.cursor()
        #create table settemp(userID int,boardID int,temp int)
        cur.execute(f"INSERT INTO settemp(userID,boardID,temp) VALUES({userID},{boardID},{temp})")
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    return render_template('index1.html')



@app.route('/currenttemp')
def users():
    cur=mysql.connection.cursor()
    cur.execute("SELECT temp FROM curnttemp")
    fetchdata = cur.fetchall()
    cur.close()
    #print(str(fetchdata))
    return '<h1>the current temperature is '+str(fetchdata[-1])+'.<h1>'


@app.route('/settemp')
def users1():
    cur=mysql.connection.cursor()
    cur.execute("SELECT temp FROM settemp")
    fetchdata1 = cur.fetchall()
    cur.close()
    #print(str(fetchdata))
    return '<h1>the current temperature is '+str(fetchdata1[-1])+'.<h1>'

if __name__=='__main__':
    app.run(debug=True)
