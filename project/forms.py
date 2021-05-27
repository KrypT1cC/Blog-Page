from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, FileField, TextAreaField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo
from project.models import Accounts
from flask_login import current_user
import json


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


# forms for changing account information


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
            EqualTo('new_password', message="New passwords don't match.")
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
            EqualTo('new_email', message='Emails do not match')
        ]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField('Change Email')

    def validate_new_email(self, value):
        user = Accounts.query.filter_by(email=value.data.lower()).first()
        if user is not None:
            raise ValidationError("Email already exists")


class ChangeProfilePictureForm(FlaskForm):
    profile_pic = FileField(
        "Choose New Profile Picture",
        validators=[
            FileRequired(message="No file attached"),
            FileAllowed(['jpg', 'png'], message='Only .jpg and .png files are allowed')
        ]
    )
    submit = SubmitField("Change Profile Picture")


# form for creating new chat


class CreateChat(FlaskForm):
    accounts = StringField(
        "Accounts",
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField('Create Chat')

    def validate_accounts(self, value):
        account_list = value.data.split(', ')
        for account in account_list:
            user = Accounts.query.filter_by(username=account).first()
            if user is None:
                raise ValidationError('Account does not exist: ' + account)
            if account not in json.loads(current_user.friends) and account != current_user.username:
                raise ValidationError('Not friends with: ' + account)


class CreatePost(FlaskForm):
    caption = TextAreaField(
        'Caption',
    )

    image = FileField(
        'Image',
        validators=[
            FileRequired(message="No file attached"),
            FileAllowed(['jpg', 'png'], message='Only .jpg and .png files are allowed')
        ]
    )
    submit = SubmitField('Post Online')


