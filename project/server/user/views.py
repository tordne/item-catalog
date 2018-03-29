# project/server/user/views.py

from flask import Blueprint, render_template, session, url_for, \
    redirect, request, flash

from project.server.helpers import login_required, credentials_to_dict

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


def getUserInfo():
    '''
    Take the credentials obtained and request the users info through google.
    '''
    credentials = session['credentials']

    response = requests.get(
        'https://www.googleapis.com/oauth2/v2/userinfo',
        params={'access_token': credentials['token']})

    data = json.loads(response.text)

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
    pg_session.add(newUser)
    pg_session.commit()
    user = pg_session.query(User).filter_by(email=login_session['email']).one()
    return user.id



''' Routes '''


@user_blueprint.route('/authorize')
def authorize():
    '''
    Create a flow instance to manage the OAuth2 Authorization Grant Flow steps

    .. :quickref: User; Create a flow instance to manage the OAuth2
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
    #pdb.set_trace()
    # Redirect the user to Google OAuth page to obtain consent
    return redirect(authorization_url)


@user_blueprint.route('/gconnect')
def oauth2callback():
    '''
    Specify the state so it can verify the server response.
    When successful, fetch the OAuth2 tokens and store the credentials

    .. :quickref: User; Fetch the Oauth2 tokens and store credentials
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

    # Retrieve userinfo with the session['credentials']
    data = getUserInfo()
    # Add the userinfo into the session dict
    session.update(data)
    # Create a logged_in key with a boolean value True
    session['logged_in'] = True

    # Flash message of correct login
    flash('User {} is authorized'.format(data['name']), 'success')

    # Redirect the user back to the main page.
    return redirect(url_for('main.list_categories'))


@user_blueprint.route('/revoke')
@login_required
def revoke():
    '''
    Revoke access to user by removing credentials token

    .. :quickref: User; Revoke user access by removing credentials
    '''
    if 'credentials' not in session:
        flash('User is not authorized', 'warning')
        return redirect(url_for('main.list_categories'))

    credentials = session['credentials']

    revoke = requests.post(
        'https://accounts.google.com/o/oauth2/revoke',
        params={'token': credentials['token']},
        headers={'content-type': 'application/x-www-form-urlencoded'}
    )

    # When successfully revoked, clear the session of all data
    session.clear()

    status_code = getattr(revoke, 'status_code')
    if status_code == 200:
        flash('Credentials successfully revoked', 'success')
        return redirect(url_for('main.list_categories'))
    else:
        flash('An error occurred', 'warning')
        # Redirect the user back to the main page.
        return redirect(url_for('main.list_categories'))
