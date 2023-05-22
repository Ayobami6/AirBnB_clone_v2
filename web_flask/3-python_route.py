#!/usr/bin/python3
""" python route
"""
from flask import Flask

app = Flask(__name__)


@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """Returns Python followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
