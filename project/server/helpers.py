# project/server/helpers.py
'''
.. module:: helpers
    :synopsis: These are global helpers used throughout the blueprints.
'''
from flask import session, redirect, url_for, flash

from project.server import pg_session
from project.server.models import User, Category, Item

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


def check_authentication(d):
    '''
    This is a decorator function which runs after the login_required.
    The function checks if the user who wants to edit or delete the item
    or category is the owner.
    If the user is not the owner a warning message will flash.
    '''
    @wraps(d)
    def wrap(*args, **kwargs):
        # Check if the "item" keyword is in the arguments
        if 'iten' in kwargs:
            # Collect the catalog from the database
            item_id = pg_session.query(Item).filter_by(
                name=kwargs['item']).one()

            if session['user_id'] == item_id.user_id:
                return d(*args, **kwargs)
            else:
                flash('You are not authorised to edit/delete this item',
                      'warning')
                return redirect(url_for('main.list_categories'))

        # Check if the "category" keyword is in the arguments
        if 'category' in kwargs:
            # Collect the catalog from the database
            cat_id = pg_session.query(Category).filter_by(
                name=kwargs['category']).one()

            if session['user_id'] == cat_id.user_id:
                return d(*args, **kwargs)
            else:
                flash('You are not authorised to edit/delete this category',
                      'warning')
                return redirect(url_for('main.list_categories'))

    return wrap


def credentials_to_dict(credentials):
    '''
    Take the credentials and return it as a dict.

    :param credentials: a constructed credentials
    :type: constructed credentials
    :return: a dict with the following keys: token, expiry, refresh, \
        token_uri, client_id, client_secret, scopes
    '''
    return {'token': credentials.token,
            'expiry': credentials.expiry,
            'refresh': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}
