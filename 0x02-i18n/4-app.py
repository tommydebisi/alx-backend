#!/usr/bin/env python3
""" 3-app mod """
from flask import Flask, request, render_template
from flask_babel import Babel, _

Config = __import__('config').Config
app = Flask(__name__)
app.config.from_pyfile('config.py')
babel = Babel(app)


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
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
