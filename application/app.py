from flask import request, redirect, url_for, Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy 
from os import getenv
import pymysql

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@35.242.179.70:3306/project_1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY' 

db = SQLAlchemy(app)
db.create_all() 

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {first_name} {last_name}'

    return render_template('home.html', form=form, message=message)

@app.route('/example/<booly>')
def example(booly):
    if booly.lower()=="yes":
        return redirect(url_for("example"))
    else:
        return "Nothing would be redirected"


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')