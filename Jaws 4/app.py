from flask import Flask,render_template,flash,request,redirect,url_for,send_file
from os import path
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField 

ROOT = path.dirname(path.realpath(__file__))

def checkPass(username,password):
    if username=='NHK' and password=='PasswordIsACTF':
        return True
    return False

app = Flask(__name__)
app.config['SECRET_KEY']='nosecretkeyforthisquestion'

class QuestionForm(FlaskForm):
    username = StringField(label='Enter Username')
    password = PasswordField(label='Enter Password')
    submit = SubmitField(label='Login')
    
class SearchForm(FlaskForm):
    text = StringField(label='Search')
    submit = SubmitField(label='Search')

@app.route('/',methods=['GET','POST'])
def home():
    form = QuestionForm()
    if request.method=='POST':
        if checkPass(username=form.username.data,password=form.password.data):
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect! Try Again!')
    return render_template('home.html',form=form)

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    form = SearchForm()
    if request.method=='POST':
        if form.text.data == 'Discovered':        
            return render_template('search.html',searched=form.text.data,correct=True)
        return render_template('search.html',searched=form.text.data)
    return render_template('dashboard.html',form=form)

@app.route('/download',methods=['GET'])
def download():
    return send_file(ROOT+'\\static\\data.txt',as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)
    
# 38th position the data file