# project/server/__init__.py

''' Flask is imported and basic configurations are set. '''
from flask import Flask

app = Flask(__name__,
            template_folder='../client/templates',
            static_folder='../client/static'
            )


''' Blueprints
All the different packages are imported and
the blueprints are registered in the app.
'''
from project.server.main.views import main_blueprint
app.register_blueprint(main_blueprint)
