from application import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(20), nullable=False)
    mode = db.Column(db.String(20), nullable=False)
    publisher = db.Column(db.String(200), nullable=False)
    release_date = db.Column(db.Date, nullable=False)

    def __init__(self, game, mode, publisher, release_date):
        self.game = game
        self.mode = mode
        self.publisher = publisher
        self.release_date = release_date


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


