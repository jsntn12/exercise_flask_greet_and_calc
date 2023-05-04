from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_page():
    return "Welcome"


@app.route('/welcome/<status>')
def welcome_message(status):
    return f"welcome {status}"