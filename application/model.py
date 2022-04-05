from application import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(20), nullable=False)
    mode = db.Column(db.String(20), nullable=False)
    publisher = db.Column(db.String(200), nullable=False)
    release_date = db.Column(db.Date, nullable=False)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    review_date = db.Column(db.Date, nullable=False)
    rating = db.Column(db.Integer)
    comments = db.Column(db.String(200), nullable=False)


if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')

