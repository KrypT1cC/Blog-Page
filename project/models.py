from project import db
from flask_login import UserMixin


class Accounts(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)

    @staticmethod
    def get(ID):
        user = Accounts.query.filter_by(id=ID).first()
        return user

