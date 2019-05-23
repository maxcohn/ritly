import os

from flask import Flask

# Main TODO
# Get DB connection working
# create DB modification and searching functions

# create template page for homepage

# design new url request style


"""App factory function

Create the Flask application. When running the
application, Flask will automatically find this function and run it,
starting the application.
"""
def create_app():
    # create and configure the app
    app = Flask(__name__)

    # include blueprints
    from . import routes

    app.register_blueprint(routes.bp)

    return app

