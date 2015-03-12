from datetime import datetime
from flask import current_app, g
from app.app import jwt
from app.main.models import User


@jwt.authentication_handler
def authenticate(username, password):
    user = User.query.filter_by(email=username).first()
    if user and user.verify_password(password):
        return user
    else:
        return None

@jwt.user_handler
def load_user(payload):
    user = User.query.get(payload['user_id'])
    g.user = user
    return user

@jwt.payload_handler
def make_payload(user):
    return {
        'user_id': user.id,
        'exp': str(datetime.utcnow() + current_app.config['JWT_EXPIRATION_DELTA'])
    }
