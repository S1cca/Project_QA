from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    publisher = db.Column(db.String(200), nullable=False)
    review_game = db.relationship('Review', backref='gamebr', lazy=True)

class AddGame(FlaskForm):
    game_name = StringField('Enter the name of the game: ')
    category = StringField('Enter the category of the game: ')
    publisher = StringField('Enter the publisher of the game: ')
    submit = SubmitField('Add Game')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False) 
    rating = db.Column(db.Integer)
    comments = db.Column(db.String(200))

class AddReview(FlaskForm):
    game_name = SelectField(u'Game', choices = [])
    rating = StringField('Please Rate the game from 1 to 5: ')
    comments = StringField('Enter your comments here: ')
    submit = SubmitField('Post Review')


