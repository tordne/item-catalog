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
    CLIENT_ID = '101XXXXXXX-l3hXXXXXXXX8e.apps.googleusercontent.com '
    CLIENT_SECRET = 'tVXXXXXXXXJ7 '


class DevelopmentConfig(BaseConfig):
    ''' Development configuration '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='postgresql://vagrant:vagrant@localhost/catalog'


class TestingConfig(BaseConfig):
    ''' Testing configuration '''
    DEBUG = False
    TESTING = True
