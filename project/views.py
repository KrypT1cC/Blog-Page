from project import app, db, bcrypt, login_manager
from project.forms import LoginForm, RegisterForm
from project.models import Accounts
from flask_login import login_required, login_user, current_user, logout_user
from flask import render_template, request, redirect, url_for, flash


@login_manager.user_loader
def load_user(user_id):
    return Accounts.get(user_id)


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        logout_user()
        return redirect(url_for('login'))
    return render_template('home.html', user=current_user.username)


@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = Accounts.query.filter_by(username=form.username.data).first()
        if user is not None:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():

    register_form = RegisterForm()

    if register_form.validate_on_submit():
        email = register_form.email.data.lower()
        username = register_form.username.data
        password = bcrypt.generate_password_hash(register_form.password.data, 15)

        new_user = Accounts(email=email, username=username, password=password)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('forgot_password'))
    return render_template('register.html', form=register_form)


@app.route('/forgot')
def forgot_password():
    return "forgot"
