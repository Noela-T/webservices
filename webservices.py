from flask import Flask, redirect, render_template, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:GSnoela18@localhost/webdb'
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']="gdewihohofc"
db = SQLAlchemy(app)
class NameForm(Form):
    name=StringField('What is your name?', validators=[Required()])
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name']=form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
