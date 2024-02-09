from flask import Flask,render_template,flash,request
import sqlite3
from os import path,urandom

ROOT = path.dirname(path.realpath(__file__))
conn = sqlite3.connect(path.join(ROOT, "data.db"),check_same_thread=False)

def create():
    cur = conn.cursor()
    table = """ CREATE TABLE IF NOT EXISTS USERS(
                username varchar(30) primary key,
                password varchar(10) not null
    );
    """
    cur.execute(table)

def checkPass(query):
    data = conn.execute(query)
    i=0
    for row in data:
        i+=1
    if i>0:
        return True
    return False

app = Flask(__name__)
app.config['SECRET_KEY']='nosecretkeyforthisquestion'

@app.route('/',methods=['GET','POST'])
def home():
    create()
    if request.method=='POST':
        query = f"SELECT * FROM USERS WHERE PASSWORD='{request.form.get('password')}' and USERNAME='{request.form.get('username')}'"
        if checkPass(query):
            print(request.form.get('csrf_token'))
            if request.form.get('csrf_token')=='abebc66d':
                flash('Good Job! Your flag is aCTF{G0t_H@Ck3D_1NdE3D}')
                return render_template('admin.html')
            data = conn.execute(query)
            return render_template('client.html',data=data)
        else:
            flash('Incorrect! Try Again!')
    token = urandom(4).hex()
    print(token)
    return render_template('home.html',token=token)

if __name__=='__main__':
    app.run(debug=True)