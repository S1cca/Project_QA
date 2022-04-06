from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    publisher = db.Column(db.String(200), nullable=False)
    release_date = db.Column(db.Date, nullable=False)

class Gameform(FlaskForm):
    game_name = StringField('Enter the name of the game: ')
    category = StringField('Enter the category of the game: ')
    publisher = StringField('Enter the publisher of the game: ')
    release_date = StringField('Enter the release date of the game: ')
    submit = SubmitField('Add Game')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    review_date = db.Column(db.Date, nullable=False)
    rating = db.Column(db.Integer)
    comments = db.Column(db.String(200), nullable=False)

    def __init__(self, game_id, review_date, rating, comments):
        self.game_id = game_id
        self.review_date = review_date
        self.rating = rating
        self.comments = comments


