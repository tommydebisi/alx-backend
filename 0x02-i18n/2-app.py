#!/usr/bin/env python3
""" 2-app mod """
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)

@babel.localselector
def get_locale() -> str:
    """ get the translation best match """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', strict_slashes=False)
def hello() -> str:
    """ simple template """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
