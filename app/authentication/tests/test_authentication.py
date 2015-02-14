# from unittest2 import TestCase
from flask.ext.testing import TestCase
from app import create_app, db
from app.authentication.authentication import verify_password
from app.main.models import User


class AuthenticationTest(TestCase):
    def create_app(self):
        return create_app('testing')

    def setUp(self):
        db.create_all()
        user = User(email='test@email.com', password='test')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_authentication_correct(self):
        self.assertTrue(verify_password('test@email.com', 'test'))

    def test_authentication_incorrect(self):
        self.assertFalse(verify_password('fake', 'fake'))
