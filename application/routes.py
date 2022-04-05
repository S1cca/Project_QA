from flask import render_template, url_for, redirect, request
from application import app, db
from application.model import Game, Review



@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template ('home.html', title='Home')

@app.route('/about')
def about():
    return render_template ('about.html', title='About')

@app.route('/add_game_info', methods=['GET', 'POST'])
def add_game_info():
    return render_template ('add_game_info.html', title='Add Game')

@app.route('/delete_game_info', methods=['GET', 'POST'])
def delete_game_info():
    return render_template ('delete_game_info.html', title='Delete Game')

@app.route('/update_game_info', methods=['GET', 'POST'])
def update_game_info():
    return render_template ('update_game_info.html', title='Update Game')
    
@app.route('/add_game_review', methods=['GET', 'POST'])
def add_game_review():
    return render_template ('add_game_review.html', title='Add Game Review')

@app.route('/delete_game_review', methods=['GET', 'POST'])
def delete_game_review():
    return render_template ('delete_game_review.html', title='Delete Game Review')

@app.route('/update_game_review', methods=['GET', 'POST'])
def update_game_review():
    return render_template ('update_game_review.html', title='Update Game Review')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
