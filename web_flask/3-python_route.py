#!/usr/bin/python3
"""this starts a flask web application
tuned on 0.0.0.0 and port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """this displays 'hello HBNB'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """this displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """this will displays 'c'"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """this displays python"""
    text = text.replace("_"," ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
