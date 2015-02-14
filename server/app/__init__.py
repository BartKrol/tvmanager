from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from settings.config import config
from flask_bootstrap import Bootstrap
from flask.ext.restful import Api

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    Bootstrap(app)

    # TODO - better solution

    from . import main, authentication
    api = Api(app)
    api.add_resource(main.resources.Episodes, '/')

    return app


# def add_resources(api):
#     add_main_resources(api)



