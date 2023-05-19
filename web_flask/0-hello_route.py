#!/usr/bin/python3
"""script that starts a Flask web application
and will display Hello HBNB!"""
from flask import Flask

# Create a Flask constructor.
# It takes name of the current module as the argument
app = Flask(__name__)

# define hello hbnb route


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns Hello HBNB!"""
    return 'Hello HBNB!'


# run if name is main on port 5000 any host
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
