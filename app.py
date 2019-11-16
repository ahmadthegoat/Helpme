# app.py
import flask
import os

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template("index.html")

app.run(
    port=int(os.getenv('PORT', 8086)),
    host=os.getenv('IP', '127.0.0.1')
)