#!/usr/bin/env python3
""" config mod """


class Config:
    """ config class """
    LANGUAGES = ['en', 'fr']


BABEL_DEFAULT_LOCALE = Config.LANGUAGES[0]
BABEL_DEFAULT_TIMEZONE = 'UTC'
