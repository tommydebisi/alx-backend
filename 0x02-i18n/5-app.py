#!/usr/bin/env python3
""" 3-app mod """
from flask import Flask, request, render_template, g
from flask_babel import Babel, _
from typing import Union, Dict

app = Flask(__name__)


class Config:
    """ config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """ returns a user's dictionary from users if present or none if not """
    login_as = request.args.get('login_as')
    if login_as and users.get(int(login_as)):
        return users.get(int(login_as))
    return None


@app.before_request
def before_request() -> None:
    """ returns the get_user func value """
    user = get_user()
    g.user = user


def get_locale() -> str:
    """ get the translation best match """
    lang_arg = request.args.get('locale')
    if lang_arg and lang_arg in Config.LANGUAGES:
        # check if lang is in the list of available languages
        return lang_arg

    return request.accept_languages.best_match(Config.LANGUAGES)


babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def hello() -> str:
    """ simple template """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
