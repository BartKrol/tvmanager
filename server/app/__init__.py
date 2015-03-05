from flask import Flask
from flask.ext.jwt import JWT
from flask.ext.sqlalchemy import SQLAlchemy
from settings.config import config
from flask_bootstrap import Bootstrap
from flask.ext.restful import Api

db = SQLAlchemy()
jwt = JWT()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    Bootstrap(app)
    jwt.init_app(app)

    # TODO - better solution
    api_url = '/api/v1'
    from . import main, auth
    api = Api(app)
    api.add_resource(main.resources.TrendingShows, api_url + '/trending')

    return app


