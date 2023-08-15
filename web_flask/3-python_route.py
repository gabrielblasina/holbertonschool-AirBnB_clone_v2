#!/usr/bin/python3
""" Web flask """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    ftxt = text.replace('_', ' ')
    return f"C {ftxt}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    formatted_txt = text.replace('_', ' ')
    return f"Python {formatted_txt}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
