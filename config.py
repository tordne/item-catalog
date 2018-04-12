# project/server/config.py

'''
This template contains all the configurations for different environments
The following classes are used according to their environment:
    * All: BaseConfig
    * Development: DevelopmentConfig
    * Testing: TestingConfig
    * Production: ProductionConfig
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    ''' Base configuration '''
    SECRET_KEY = 'very_secret_key'
    DEBUG = False
    TESTING = False
    # Google OAuh2.0
    CLIENT_ID = '1018639020947-l3h0bppvstv799dijbdiuot9a86bce8e.apps.googleusercontent.com'  # NOQA
    CLIENT_SECRET = 'tVHNcNnAf5drQJBBlcrTRhJ7'
    CLIENT_SECRET_FILE = os.environ['CLIENT_SECRET_FILE']
    SCOPES = ['https://www.googleapis.com/auth/userinfo.profile',
              'https://www.googleapis.com/auth/userinfo.email']
    OAUTHLIB_INSECURE_TRANSPORT = '1'


class DevelopmentConfig(BaseConfig):
    ''' Development configuration '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']  # NOQA
    OAUTHLIB_INSECURE_TRANSPORT = '1'


class TestingConfig(BaseConfig):
    ''' Testing configuration '''
    DEBUG = False
    TESTING = True
