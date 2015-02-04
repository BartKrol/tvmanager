from flask import render_template

from . import authentication

@authentication.route('/login')
def login():
    return render_template('authentication/login.html')