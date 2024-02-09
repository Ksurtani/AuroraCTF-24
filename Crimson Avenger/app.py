from flask import Flask,render_template,request
from wtforms import StringField,SubmitField
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY']='nosecretkeyforthisquestion'

class RegexForm(FlaskForm):
    text = StringField(label='Enter Text: ')
    submit = SubmitField(label='Submit')
  
@app.route('/',methods=['GET','POST'])
def home():
    print(request.headers)
    print(request.headers.get('Flag'))
    form = RegexForm()
    return render_template('home.html',form=form)

@app.after_request
def add_header(response):
    response.headers['Flag']='aCTF{R3d_D3@d_r3D3m7t10n}'
    return response

if __name__=='__main__':
    app.run(debug=True)