from flask import g
from flask.ext.httpauth import HTTPBasicAuth
from app.main.models import User

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if not user:
        return False
    g.current_user = user
    return user.verify_password(password)

# TODO - token authentication
# @auth.verify_password
# def verify_password(email_or_token, password):
#     if email_or_token == '':
#         g.current_user = AnonymousUser()
#         return True
#     if password == '':
#         g.current_user = User.verify_auth_token(email_or_token)
#         g.token_used = True
#         return g.current_user is not None
#     user = User.query.filter_by(email=email_or_token).first()
#     if not user:
#         return False
#     g.current_user = user
#     g.token_used = False
#     return user.verify_password(password)


# @auth.error_handle
# def auth_error():
#     return unauthorized('Invalid credentials')

