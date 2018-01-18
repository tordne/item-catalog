# project/server/__init__.py

import os
import pdb

from flask import Flask


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


''' Blueprints
All the different packages are imported and
the blueprints are registered in the app.
'''

from project.server.main.views import main_blueprint
app.register_blueprint(main_blueprint)
