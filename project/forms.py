from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, FileField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo
from project.models import Accounts


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = StringField(
        'Email Address',
        validators=[
            DataRequired(),
            Email(message="Not a valid email")
        ]
    )
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=6, max=50, message="Username does not meet length requirements")
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8, max=100, message="Password does not meet length requirements")
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            Length(max=100),
            EqualTo('password', message="Passwords don't match")
        ]
    )
    submit = SubmitField('Register')

    def validate_email(self, field):
        user = Accounts.query.filter_by(email=field.data.lower()).first()
        if user is not None:
            raise ValidationError("Email already exists")

    def validate_username(self, field):
        user = Accounts.query.filter_by(username=field.data).first()
        if user is not None:
            raise ValidationError("Username already exists")


class ChangeUsernameForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=6, max=50, message="Username does not meet length requirements")
        ]
    )
    confirm_username = StringField(
        'Confirm Username',
        validators=[
            DataRequired(),
            EqualTo("username", message="Usernames don't match")
        ]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField('Change Username')

    def validate_username(self, value):
        user = Accounts.query.filter_by(username=value.data).first()
        if user is not None:
            raise ValidationError("Username already exists")


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField(
        "Current Password",
        validators=[
            DataRequired()
        ]
    )
    new_password = StringField(
        "New Password",
        validators=[
            DataRequired(),
            Length(min=8, max=100, message="Password does not meet length requirements")
        ]
    )
    confirm_password = StringField(
        "Confirm New Password",
        validators=[
            DataRequired(),
            EqualTo('new_password')
        ]
    )
    submit = SubmitField("Change Password")


class ChangeEmailForm(FlaskForm):
    new_email = StringField(
        "New Email",
        validators=[
            DataRequired(),
            Email(message="Not a valid email"),
        ]
    )
    confirm_email = StringField(
        "Confirm Email",
        validators=[
            DataRequired(),
            EqualTo('new_email')
        ]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField('Change Email')


class ChangeProfilePictureForm(FlaskForm):
    profile_pic = FileField(
        "Choose New Profile Picture",
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'png'], message='Only .jpg and .png files are allowed')
        ]
    )
    submit = SubmitField("Change Profile Picture")
