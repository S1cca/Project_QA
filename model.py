from app import db


class Current_Account(db.model):
    id = db.Column(db.Integer, primary_key=True)
    


class Saving_Account(db.model):
    id = db.Column(db.Integer, primary_key=True)
