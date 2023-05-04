# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = request.args.get("a")
    b = request.args.get("b")
    result = add(int(a), int(b))

    return str(result)

@app.route('/sub')
def subtract():
    a = request.args.get("a")
    b = request.args.get("b")
    result = sub(int(a), int(b))

    return str(result)

@app.route('/mult')
def multiply():
    a = request.args.get("a")
    b = request.args.get("b")
    result = mult(int(a), int(b))

    return str(result)

@app.route('/div')
def divide():
    a = request.args.get("a")
    b = request.args.get("b")
    result = div(int(a), int(b))

    return str(result)