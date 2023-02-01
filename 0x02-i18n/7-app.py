#!/usr/bin/env python3
""" 3-app mod """
from flask import Flask, request, render_template, g, session
from flask_babel import Babel, _
from typing import Dict, Union
import pytz

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
    if login_as:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request() -> None:
    """ returns the get_user func value """
    user = get_user()
    g.user = user


def get_locale() -> str:
    """ get the translation best match """
    lang_arg = None
    if g.user:
        lang_arg = g.user.get('locale')
    elif session.get('locale'):
        lang_arg = session.get('locale')
    elif request.args.get('locale'):
        lang_arg = request.args.get('locale')
    if lang_arg and lang_arg in Config.LANGUAGES:
        # check if lang is in the list of available languages
        return lang_arg
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_timezone() -> str:
    """ gets the timezone of user """
    if g.user:
        time_z = g.user.get('timezone')
    elif session.get('timezone'):
        time_z = session.get('timezone')
    try:
        if time_z:
            pytz.timezone(time_z)
            return time_z
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return 'UTC'


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/', strict_slashes=False)
def hello():
    """ simple template """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
