from project import app
from project.forms import LoginForm, RegisterForm
from flask import render_template, request, redirect, url_for


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
    if request.method == 'POST' and register_form.validate_on_submit():
        print('requirements fulfilled')

    return render_template('register.html', form=register_form)


@app.route('/forgot')
def forgot_password():
    return "forgot"
