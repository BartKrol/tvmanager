from flask import Blueprint

authentication = Blueprint('auth', __name__)

from . import views
