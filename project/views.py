from project import app
from flask import render_template, request


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request
    return render_template('home.html')


@app.route('/register')
def register():
    return "register"


@app.route('/forgot')
def forgot_password():
    return "forgot"
