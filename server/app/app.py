from flask import Flask
from settings.config import config
from .extensions import jwt, db, migrate, bootstrap
from flask.ext.restful import Api

def create_app(config_name):
    """Create a flask app from a config"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    register_extensions(app)

    # TODO - better solution
    api = Api(app)

    api_url = '/api/v1'

    from .main import resources

    # TODO - Is this needed
    from . import  auth
    api.add_resource(resources.TrendingShows, api_url + '/trending')

    return app

def register_extensions(app):
    """Register flask extensions"""
    db.init_app(app)
    bootstrap.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    return None


