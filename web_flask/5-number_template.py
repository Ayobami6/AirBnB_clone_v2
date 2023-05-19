#!/usr/bin/python3
"""script that renders a template"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Returns n is a number only if n is an integer"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
