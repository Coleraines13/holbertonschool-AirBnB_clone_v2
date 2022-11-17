#!/usr/bin/python3
"""this Write a script that starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    """removes current sql session after request"""
    storage.close()


@app.route("/cities_by_states")
def cities_by_states():
    """this displays an html page"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)
