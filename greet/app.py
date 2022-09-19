from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def make_welcome():
    return "welcome"

@app.route('/welcome/home')
def make_welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def make_welcome_back():
    return "welcome back"
