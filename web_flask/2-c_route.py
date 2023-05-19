#!/usr/bin/python3
""" C route
"""
from flask import Flask

app = Flask(__name__)


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Returns C followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
