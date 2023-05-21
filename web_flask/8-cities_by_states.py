#!/usr/bin/python3
""" States and cites endpoint
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_states_route():
    """ Cities and states route
    """
    states = storage.all("State")
    # cities = storage.all("City")

    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def tearDown(exception):
    """ Closes storage session

    Args:
        exception (TYPE): Description
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
