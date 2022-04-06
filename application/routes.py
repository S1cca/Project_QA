from flask import render_template, url_for, redirect, request
from application import app, db
from application.model import Game, Review, Gameform
from application.forms import add_game_info, delete_game_info, update_game_info, add_game_review, delete_game_review, update_game_review


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template ('home.html', title='Home')

@app.route('/about')
def about():
    return render_template ('about.html', title='About')

@app.route('/add_game_info', methods=['GET', 'POST'])
def add_game_info():
    form = Gameform()
    if form.validate_on_submit():
        new_game = Game(game_name=form.game_name.data, 
                    category=form.category.data, 
                    publisher=form.publisher.data, 
                    release_date=form.release_date.data)
        db.session.add(new_game)
        db.session.commit()
        return render_template('home.html', message = 'Game Added!')
    else:
        return render_template('add_game_info.html', form=form)    
        #     return redirect(url_for('home'))
        # else:
        #     message = 'Error: Game not added!'
        

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