from flask import Blueprint
from flask.ext import restful
main = Blueprint('main', __name__)

api = restful.Api(main)

from . import views, models

