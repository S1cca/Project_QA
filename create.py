from application import db
from application.model import Game, Review
import sqlalchemy
import pymysql
from os import getenv

db.drop_all()
db.create_all()


game1 = Game(game="Elden Ring", mode='ARPG', publisher="From Software", release_date="2022-02-25")
db.session.add(game1)
comment1 = Review(game_id=1, review_date="2020-01-01", rating=5, comments="This is a great game!")
db.session.add(comment1)
game2 = Game(game="League of Legend", mode='MMORPG', publisher="Riot", release_date="2009-10-27")
db.session.add(game2)

db.session.commit()
