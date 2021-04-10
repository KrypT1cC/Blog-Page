from project import app, db, bcrypt, login_manager
from project.forms import LoginForm, RegisterForm, ChangeUsernameForm, ChangePasswordForm, ChangeEmailForm, \
    ChangeProfilePictureForm
from project.models import Accounts
from flask_login import login_required, login_user, current_user, logout_user
from flask import render_template, request, redirect, url_for, flash
import json


@login_manager.user_loader
def load_user(user_id):
    return Accounts.get(user_id)


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        if request.form['logout'] == 'Logout':
            logout_user()
            return redirect(url_for('login'))
    return render_template('home.html', user=current_user)


@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    error = None
    form = LoginForm()
    if form.validate_on_submit():
        user = Accounts.query.filter_by(username=form.username.data).first()
        if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            error = "* Invalid login credentials."
    return render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():

    register_form = RegisterForm()

    if register_form.validate_on_submit():
        email = register_form.email.data.lower()
        username = register_form.username.data
        password = bcrypt.generate_password_hash(register_form.password.data, 15)
        friends = []
        profile_picture = '/static/img/no-profile.jpg'

        new_user = Accounts(
            email=email,
            username=username,
            password=password,
            friends=json.dumps(friends),
            profile_picture=profile_picture
        )

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('forgot_password'))
    return render_template('register.html', form=register_form)


@app.route('/forgot')
def forgot_password():
    return "forgot"


@app.route('/dm', methods=['GET', 'POST'])
@login_required
def dm():
    if request.method == 'POST':
        if request.form['logout'] == 'Logout':
            logout_user()
            return redirect(url_for('login'))
    return render_template('dms.html', user=current_user, friends=json.loads(current_user.friends))


@app.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    if request.method == 'POST':
        if request.form['logout'] == 'Logout':
            logout_user()
            return redirect(url_for('settings'))
    user = Accounts.query.filter_by(username=username).first()
    return render_template('profile.html', user=current_user, friends=json.loads(user.friends), viewed_user=user)


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def profile_settings():
    change_user_form = ChangeUsernameForm()
    change_password_form = ChangePasswordForm()
    change_email_form = ChangeEmailForm()
    change_pic_form = ChangeProfilePictureForm()

    error = None

    if request.form.get('submit') == 'Change Username':
        if change_user_form.validate_on_submit():
            if bcrypt.check_password_hash(current_user.password, change_user_form.password.data):
                current_user.username = change_user_form.username.data
                db.session.commit()
                return redirect(url_for('home'))
            else:
                error = "Password is incorrect"
    elif request.form.get('submit') == 'Change Password':
        if change_password_form.validate_on_submit():
            if bcrypt.check_password_hash(current_user.password, change_password_form.current_password.data):
                current_user.password = bcrypt.generate_password_hash(change_password_form.new_password.data, 15)
                db.session.commit()
                return redirect(url_for('home'))
            else:
                error = "Password is incorrect"

    return render_template(
        'profile_settings.html',
        user=current_user,
        change_user_form=change_user_form,
        change_password_form=change_password_form,
        change_email_form=change_email_form,
        change_pic_form=change_pic_form,
        error=error
    )
