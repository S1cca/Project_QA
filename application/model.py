from app import db


class Current_Account(db.model):
    C_id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float)
    account_number = db.Column(db.Integer)
    account_type = db.Column(db.String(20))
    account_open_date = db.Column(db.Date)



class Saving_Account(db.model):
    S_id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float)
    account_number = db.Column(db.Integer)
    account_type = db.Column(db.String(20))
    account_status = db.Column(db.String(20))
    account_open_date = db.Column(db.Date)

