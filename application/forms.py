from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from application.model import Game, Review

class add_game_info(FlaskForm):
    game_name = StringField('Game Name', validators=[DataRequired(), Length(min=2, max=20)])
    category = StringField('category', validators=[DataRequired(), Length(min=2, max=20)])
    publisher = StringField('Publisher', validators=[DataRequired(), Length(min=2, max=200)])
    release_date = StringField('Release Date', validators=[DataRequired()])
    submit = SubmitField('Press to Add Game')

class delete_game_info(FlaskForm):
    game = SelectField(u'Game',choice = [])
    submit = SubmitField('Press to Delete Game')

class update_game_info(FlaskForm):
    game = SelectField(u'Game',choice = [])
    game_name = StringField('Game Name', validators=[DataRequired(), Length(min=2, max=20)])
    category = StringField('Category', validators=[DataRequired(), Length(min=2, max=20)])
    publisher = StringField('Publisher', validators=[DataRequired(), Length(min=2, max=200)])
    release_date = StringField('Release Date', validators=[DataRequired()])
    submit = SubmitField('Press to Update Game')

class add_game_review(FlaskForm):
    game = SelectField('Game')
    review_date = StringField('Review Date', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=10)])
    comments = StringField('Comments', validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Press to Add Game Review')

class delete_game_review(FlaskForm):
    review = SelectField('Review')
    submit = SubmitField('Press to Delete Game Review')

class update_game_review(FlaskForm):
    review = SelectField('Review')
    review_date = StringField('Review Date', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=10)])
    comments = StringField('Comments', validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Press to Update Game Review')