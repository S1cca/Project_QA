from flask import render_template, url_for, redirect, request
from application import app, db
from application.model import Game, Review



@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template ('home.html', title='Home')


@app.route('/about')
def about():
    return "This is the About Page"

@app.route('/add game', methods=['GET', 'POST'])
def add_Game():
    New_Game = Game(name="New Game", mode=1, Publisher="New Publisher", release_date="2019-01-01")
    db.session.add(New_Game)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/read')
def read():
    all_games = Game.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>" + game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Game.query.first()
    first_game.name = name
    db.session.commit()
    print (f"Updated {first_game.name}")
    return render_template('home.html')
    
@app.route('/delete/<name>')
def delete(name):
    first_game = Game.query.first()
    db.session.delete(first_game)
    db.session.commit()
    print (f"{first_game.name} has been successfully deleted")
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
