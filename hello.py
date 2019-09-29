from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Gaurav'


@app.route("/2022")
def marriage():
    return "Happy married life."

@app.route("/kidsname")
def kidname():
    return "Boy or Girl."


@app.route("/wannaBeFather")
def papa():
    return 'Yes with her.'