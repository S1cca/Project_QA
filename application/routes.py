from flask import render_template, url_for, redirect, request
from application import app, db
from application.model import Game, Review, AddGame, AddReview
from application.forms import add_game_info, delete_game_info, update_game_info, add_game_review, delete_game_review, update_game_review


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    all_games = Game.query.all()
    return render_template('home.html', all_games=all_games)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/add_game_info', methods=['GET', 'POST'])
def add_game_info():
    form = AddGame()
    if request.method == 'POST':
        new_game = Game(game_name=form.game_name.data, 
                    category=form.category.data, 
                    publisher=form.publisher.data)
        db.session.add(new_game)
        db.session.commit()
        return render_template('home.html', all_games=Game.query.all())
    else:
        return render_template('add_game_info.html', form=form)    
        

@app.route('/delete_game_info/<game_name>', methods=['GET', 'POST'])
def delete_game_info(game_name):
    game = Game.query.filter_by(game_name=game_name).first()
    if game:
        db.session.delete(game)
        db.session.commit()
        return render_template('home.html', all_games=Game.query.all())
    return render_template ('home.html', all_games=Game.query.all())

@app.route('/add_game_review', methods=['GET', 'POST'])
def add_game_review():
    form = AddReview()
    form.game_name.choices = [(game.id, game.game_name) for game in Game.query.all()]
    if form.validate_on_submit():
        new_review = Review(rating = form.rating.data,
                            game_id = form.game_name.data, 
                            comments = form.comments.data)
        db.session.add(new_review)
        db.session.commit()
        return render_template('reviewlist.html', all_reviews=Review.query.all())
    else:
        return render_template ('add_game_review.html', form = form)

@app.route('/delete_game_review/<game_id>', methods=['GET', 'POST'])
def delete_game_review(game_id):
    message = " "
    review = Review.query.filter_by(game_id=game_id).first()
    if review:
        db.session.delete(review)
        db.session.commit()
        return render_template('home.html', message = 'Review Deleted!')
    return render_template ('reviewlist.html', all_reviews=Review.query.all())

@app.route('/reviewlist', methods=['GET', 'POST'])
def reviewlist():
    all_reviews = Review.query.all()
    return render_template ('reviewlist.html', all_reviews=all_reviews)

@app.route('/update_game_review', methods=['GET', 'POST'])
def update_game_review():
    return render_template ('update_game_review.html', title='Update Game Review')
    
@app.route('/update_game_info', methods=['GET', 'POST'])
def update_game_info():
    return render_template ('update_game_info.html', title='Update Game')