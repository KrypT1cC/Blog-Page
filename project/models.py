from project import db
from flask_login import UserMixin


class Accounts(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    profile_picture = db.Column(db.String(), unique=False, nullable=False)
    followers = db.Column(db.String(), unique=False, nullable=True)
    following = db.Column(db.String(), unique=False, nullable=True)
    friends = db.Column(db.String(), unique=False, nullable=True)
    chats = db.relationship('Messages', backref='account')

    @staticmethod
    def get(ID):
        user = Accounts.query.filter_by(id=ID).first()
        return user


class Messages(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    chat_name = db.Column(db.String(), unique=False, nullable=False)
    accounts = db.Column(db.String(), unique=True, nullable=False)
    messages = db.Column(db.String(), unique=False, nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
