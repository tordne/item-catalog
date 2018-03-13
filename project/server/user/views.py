# project/server/user/views.py

from google_auth_oauthlib.flow import Flow
import requests
import os
import pdb

from flask import Blueprint, render_template, session, url_for, \
    redirect, current_app, request


''' Configuration '''


user_blueprint = Blueprint('user', __name__,)


CLIENT_SECRET_FILE = '/vagrant/client_secret.json'
SCOPES = ['profile', 'email']

''' Routes '''


@user_blueprint.route('/authorize')
def authorize():
    '''
    Create a flow instance to manage the OAuth2 Authorization Grant Flow steps

    '''
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE, scopes=SCOPES)

    flow.redirect_uri = url_for('.oauth2callback', _external=True)

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
    When successful fetch the OAuth2 tokens and store the credentials
    '''
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    state = session['state']

    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = url_for('.oauth2callback', _external=True)

    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials

    return redirect(url_for('main.list_categories'))
