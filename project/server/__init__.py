# project/server/__init__.py

import os
import pdb

from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from project.server.models import Base, User, Category, Item, Credential
from project.server.helpers import login_required, credentials_to_dict


''' Create Flask instance and set Application Environment
through the APP_SETTINGS environmental variable.
'''

app = Flask(__name__,
            template_folder='../client/templates',
            static_folder='../client/static',
            instance_relative_config=True
            )

app_settings = os.getenv(
    'FLASK_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(app_settings)
app.config.from_envvar('FLASK_CONFIG')


''' SQLAlchemy: Create engine, Bind tables, setup staging zone
and create a session
'''

# Create an engine connecting to the DB
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# Bind the tables metadata to the engine
Base.metadata.bind = engine

# Create a staging zone with the engine
DBSession = sessionmaker(bind=engine)
# Create a session connecting to the staging zone
pg_session = DBSession()


''' Blueprints
All the different packages are imported and
the blueprints are registered in the app.
'''

from project.server.main.views import main_blueprint
app.register_blueprint(main_blueprint)
from project.server.user.views import user_blueprint
app.register_blueprint(user_blueprint)
