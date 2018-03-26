# project/server/user/views.py

from flask import Blueprint, render_template, session, url_for, \
    redirect, request, flash
from functools import wraps

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow

import requests
import json

import os
import pdb


''' Configuration '''


user_blueprint = Blueprint('user', __name__,)


CLIENT_SECRET_FILE = '/vagrant/client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/userinfo.profile',
          'https://www.googleapis.com/auth/userinfo.email']


''' Helper Functions '''


def login_required(f):
    '''
    Make routes private, for logged_in user only.
    Check if the user is logged in, if True continue to the route.
    Else give a warning to log in first and redirect to the main route.
    '''
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.', 'warning')
            return redirect(url_for('main.list_categories'))
    return wrap


def getUserInfo():
    '''
    Take the credentials obtained and request the users info through google.
    '''
    credentials = session['credentials']

    response = requests.get(
        'https://www.googleapis.com/oauth2/v2/userinfo',
        params={'access_token': credentials['token']})

    data = json.loads(response.text)
    # pdb.set_trace()
    status_code = getattr(response, 'status_code')
    if status_code == 200:
        return data
    else:
        flash('Could not load the user info', 'warning')
        return redirect(url_for('main.list_categories'))


def createUser(session):
    newUser = User(
        name=login_session['username'],
        email=login_session['email'],
        picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def credentials_to_dict(credentials):
    return {'token': credentials.token,
            'refresh': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}


''' Routes '''


@user_blueprint.route('/authorize')
def authorize():
    '''
    Create a flow instance to manage the OAuth2 Authorization Grant Flow steps
    '''

    # Create the flow instance using the client secret file
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE, scopes=SCOPES)
    # Add the redirect_uri to the oauth2session
    flow.redirect_uri = url_for('.oauth2callback', _external=True)

    # Generate the Authorization URL. Step 1 in the Oauth2.0 Authorization Flow
    authorization_url, state = flow.authorization_url(
        # Enable offline access to prevent re-prompting the user for permission
        access_type='offline',
        # Enable incremental authorization.
        include_granted_scopes='true')

    # Store the state in the session to verify the callback.
    session['state'] = state

    # Redirect the user to Google OAuth page to obtain consent
    return redirect(authorization_url)


@user_blueprint.route('/gconnect')
def oauth2callback():
    '''
    Specify the state so it can verify the server response.
    When successful, fetch the OAuth2 tokens and store the credentials
    '''

    # In a development environment allow insecure transport
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    state = session['state']

    # Create the flow instance using the client secret file, scope and state
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE, scopes=SCOPES, state=state)
    # Add the redirect uri to the flow.oauth2session
    flow.redirect_uri = url_for('.oauth2callback', _external=True)

    # Create the authorization url to obtain the access token
    authorization_response = request.url
    # Complete the Authorization Flow and obtain an access token
    flow.fetch_token(authorization_response=authorization_response)

    # Create an credentials instance using session's tokens and client config
    credentials = flow.credentials

    # PLACE ALL TOKENS IN THE DATABASE
    session['credentials'] = credentials_to_dict(credentials)

    data = getUserInfo()
    # pdb.set_trace()
    # Flash message of correct login
    flash('User {} is authorized'.format(data['name']), 'success')

    # Redirect the user back to the main page.
    return redirect(url_for('main.list_categories'))


@user_blueprint.route('/revoke')
def revoke():
    if 'credentials' not in session:
        flash('User is not authorized')
        return "You need to authorize first"

    credentials = session['credentials']

    revoke = requests.post(
        'https://accounts.google.com/o/oauth2/revoke',
        params={'token': credentials['token']},
        headers={'content-type': 'application/x-www-form-urlencoded'}
    )

    status_code = getattr(revoke, 'status_code')
    if status_code == 200:
        flash('Credentials successfully revoked', 'success')
        return redirect(url_for('main.list_categories'))
    else:
        flash('An error occurred', 'warning')
        # Redirect the user back to the main page.
        return redirect(url_for('main.list_categories'))
