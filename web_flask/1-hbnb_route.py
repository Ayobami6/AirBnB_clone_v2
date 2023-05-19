#!/usr/bin/python3
""" HBNB route
"""
from flask import Flask

# Create a Flask constructor.
# It takes name of the current module as the argument
app = Flask(__name__)

# hnbn route


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
