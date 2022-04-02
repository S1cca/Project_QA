from flask import Flask, render_template, request, redirect, url_for
import os
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@34.142.88.205:3306/flask_example_db"

app = Flask(__name__)

@app.route('/')
# @app.route('/home', methods=['GET', 'POST'])
# def home():
#     return "Hello World!"

@app.route('/home')
def home():
    return f"Hello World!"

@app.route('/about')
def about():
    return 'ABOUT PAGE'

@app.route('/account')
def account():
    return render_template('account.html', title='My Account')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)