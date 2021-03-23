from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SOME_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////accounts.db'

db = SQLAlchemy(app)

from project.models import *
# db.create_all()

import project.views
