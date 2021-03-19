from project.setup import app

@app.route('/')
def home():
    return 'This is the home page.'
