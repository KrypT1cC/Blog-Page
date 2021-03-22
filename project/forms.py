from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=50)])
    password = PasswordField('password', validators=[DataRequired(), Length(max=100)])