from project import db
from flask_login import UserMixin


chats = db.Table(
    'chats',
    db.Column('user_id', db.Integer, db.ForeignKey('accounts.id'), primary_key=True),
    db.Column('chat_id', db.Integer, db.ForeignKey('messages.id'), primary_key=True)
)


class Accounts(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    profile_picture = db.Column(db.String(), unique=False, nullable=False)
    followers = db.Column(db.String(), unique=False, nullable=True)
    following = db.Column(db.String(), unique=False, nullable=True)
    friends = db.Column(db.String(), unique=False, nullable=True)

    # backref is referenced in the Messages class
    chats = db.relationship('Messages', secondary=chats, backref=db.backref('chat_users', lazy='dynamic'))

    @staticmethod
    def get(ID):
        user = Accounts.query.filter_by(id=ID).first()
        return user


class Messages(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    chat_name = db.Column(db.String(), unique=False, nullable=False)
    accounts = db.Column(db.String(), unique=True, nullable=False)
    messages = db.Column(db.String(), unique=False, nullable=True)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator = db.Column(db.String(), unique=False, nullable=False)
    caption = db.Column(db.String(), unique=False, nullable=False)
    likes = db.Column(db.Integer(), unique=False, nullable=False)
    comments = db.Column(db.String(), unique=False, nullable=True)
    image = db.Column(db.String(), unique=False, nullable=True)