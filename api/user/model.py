from api import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(10), nullable=False)

    '''def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email'''
