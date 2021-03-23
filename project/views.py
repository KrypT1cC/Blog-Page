from project import app
from project.forms import LoginForm
from flask import render_template, request, redirect, url_for


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()

    if request.method == 'POST':
        print(form.password.data)
        if form.username.data == "username" and form.password.data == "password":
            return redirect(url_for('forgot_password'))
    return render_template('home.html', form=form)


@app.route('/register')
def register():
    return "register"


@app.route('/forgot')
def forgot_password():
    return "forgot"
