from project import app, db, bcrypt
from project.forms import LoginForm, RegisterForm
from project.models import Accounts
from flask import render_template, request, redirect, url_for, flash


@app.route('/', methods=['GET', 'POST'])
def home():

    form = LoginForm()

    if request.method == 'POST':
        if form.username.data == "username" and form.password.data == "password":
            return redirect(url_for('forgot_password'))
    return render_template('home.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():

    register_form = RegisterForm()

    if register_form.validate_on_submit():
        email = register_form.email.data.lower()
        username = register_form.username.data
        password = bcrypt.generate_password_hash(register_form.password.data, 15)

        userE = Accounts.query.filter_by(email=email).first()
        userU = Accounts.query.filter_by(username=username).first()

        if userE is None and userU is None:
            new_user = Accounts(email=email, username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('forgot_password'))
    return render_template('register.html', form=register_form)


@app.route('/forgot')
def forgot_password():
    return "forgot"
