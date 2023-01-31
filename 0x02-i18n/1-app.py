#!/usr/bin/env python3
"""
    1-app mod
"""
from flask import Flask, render_template
from flask_babel import Babel

Config = __import__('config').Config
app = Flask(__name__)
app.config.from_pyfile('config.py')
babel = Babel(app)


@app.route('/', strict_slashes=False)
def hello() -> str:
    """ simple template """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
