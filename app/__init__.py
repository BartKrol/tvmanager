from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from settings.config import config
from flask_bootstrap import Bootstrap
from flask.ext.restful import Resource, Api

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    Bootstrap(app)

    # TODO - better solution
    from main import main as main_blueprint

    # app.register_blueprint(main_blueprint, template_folder='templates')
    #
    # from authentication import authentication as authentication_blueprint
    #
    # app.register_blueprint(authentication_blueprint, template_folder='templates')

    return app
