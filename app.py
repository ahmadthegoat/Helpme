# app.py
import flask
import os
from flask_bootstrap import Bootstrap

app = flask.Flask(__name__)
Bootstrap(app)
@app.route('/')
def index():
    return flask.render_template("index.html")


@app.route('/resources')
def resources():
    return flask.render_template("base.html")

@app.route('/contact')
def contact():
    return flask.render_template("contact.html")
app.run(
    port=int(os.getenv('PORT', 8085)),
    host=os.getenv('IP', '127.0.0.1')
)

if __name__ == '__main__':
    app.run(debug=True)
