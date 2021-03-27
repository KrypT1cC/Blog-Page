from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email(message="Not a valid email"), validate()])
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=50, message="Username too short")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=100, message="Password is too short")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(max=100), EqualTo('password', message="Passwords don't match")])
    submit = SubmitField('Register')



