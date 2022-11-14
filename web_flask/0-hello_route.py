#!/usr/bin/python3
"""this will start a flask web application tuned
to 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """this displays "hello hbnb"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
