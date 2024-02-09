from flask import Flask,render_template,flash,request
from wtforms import StringField,SubmitField
from flask_wtf import FlaskForm

def checkPass(password):
    if password == '379411500469':
        return True
    return False

app = Flask(__name__)
app.config['SECRET_KEY']='nosecretkeyforthisquestion'

class RegexForm(FlaskForm):
    text = StringField(label='Enter Text: ')
    submit = SubmitField(label='Submit')

@app.route('/',methods=['GET','POST'])
def home():
    form = RegexForm()
    if request.method=='POST':
        if checkPass(password=form.text.data):
            flash('Good Job! Your flag is djcj{mbbs_sludok_ki_sfxpegzng}')
        else:
            flash('Incorrect! Try Again!')
    return render_template('home.html',form=form)

if __name__=='__main__':
    app.run(debug=1)