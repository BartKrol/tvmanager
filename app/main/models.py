from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    series = relationship("series_of_user", order_by="series_of_user.id", backref="user")
    def __repr__(self):
        return '<User {0}>'.format(self.email)

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class SeriesOfUser(db.Model):
    __tablename__ = 'series_of_user'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    series_id = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<series_for_user (0)>'.format(self.user_id, self.series_id)

    @property
    def series_id(self):
        return self.series_id