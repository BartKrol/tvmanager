# -*- coding: utf-8 -*-
"""nose2 testing layers"""
from app.app import create_app, db
from app.main.models import User

class AppLayer(object):
    """Main Flask application layer"""
    @classmethod
    def setUp(cls):
        """Required to be recognised as a layer"""
        pass

    @classmethod
    def testSetUp(cls, test):
        """Set up the flask app per test case"""
        test.app = create_app('testing')
        test.app_context = test.app.app_context()
        test.app_context.push()

    @classmethod
    def testTearDown(cls, test):
        """Tear down the flask app per test case"""
        test.app_context.pop()


class DbLayer(AppLayer):
    """Database sub-layer"""

    @classmethod
    def setUp(cls):
        """Required to be recognised as a layer"""
        pass

    @classmethod
    def testSetUp(cls, test):
        """Set up the database per test case"""
        db.create_all()
        test.user = User(email='test@email.com', password='test')
        db.session.add(test.user)
        db.session.commit()

    @classmethod
    def testTearDown(cls, test):
        """Tear down the database per test case"""
        db.session.remove()
        db.drop_all()


