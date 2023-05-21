#!/usr/bin/python3
""" Renders states list from mysql database
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ States list endpoint
    """
    states = storage.all('State')
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tearDown(exception):
    """ close db sessions

    Args:
        exc (TYPE): Description
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
