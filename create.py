from application import db
from application.model import Game, Review
import sqlalchemy
import pymysql
from os import getenv

db.drop_all()
db.create_all()


game1 = Game(game_name="Elden Ring", category='ARPG', publisher="From Software")
db.session.add(game1)
game2 = Game(game_name="League of Legend", category='MMORPG', publisher="Riot")
db.session.add(game2)

db.session.commit()
