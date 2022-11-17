#!/usr/bin/python3
"this starts a script that starts a Flask web application"

from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """this will take down the app after session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """this will display a list of states"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    """this connects to the server"""
    app.run(host="0.0.0.0", port=5000)
