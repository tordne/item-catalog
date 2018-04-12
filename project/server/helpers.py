# project/server/helpers.py
'''
.. module:: helpers
    :synopsis: These are global helpers used throughout the blueprints.
'''
from flask import session, redirect, url_for, flash

from functools import wraps

import pdb


def login_required(f):
    '''
    Make routes private, for logged_in user only.
    Check if the user is logged in, if True continue to the route.
    Else give a warning to log in first and redirect to the main route.

    :param f: The wrapped function
    :type: function
    '''
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.', 'warning')
            return redirect(url_for('main.list_categories'))
    return wrap


def credentials_to_dict(credentials):
    '''
    Take the credentials and return it as a dict.

    :param credentials: a constructed credentials
    :type: constructed credentials
    :return: a dict with the following keys: token, expiry, refresh, token_uri, \
        client_id, client_secret, scopes
    '''
    return {'token': credentials.token,
            'expiry': credentials.expiry,
            'refresh': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}
