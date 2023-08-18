#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays 'C <text>'
    /python/<text> Displays 'Python <text>' if no text default="is cool"
    /number/<n> Displays "<n> is a number"
    /number_template/<n> Displays HTML page if <n> is a number
    /number_odd_or_even/<n> Displays HTML page if <n> is a number odd or even
"""

from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB!'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Displays C <text>!"""
    with_space = text.replace('_', ' ')
    return f'C {escape(with_space)}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Displays Python is cool or Python <text>"""
    with_space = text.replace('_', ' ')
    return f'Python {escape(with_space)}'


@app.route('/number/<int:n>', strict_slashes=False)
def integer_route(n):
    """Displays <n> is a number"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_tamplate_route(n):
    """Displays HTML page if n is a number"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_route(n):
    """Displays HTML page if n is odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
