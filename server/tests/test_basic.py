from flask import current_app
from unittest2 import TestCase
from app.app import create_app


class BasicTestCase(TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)
        self.assertFalse(self.app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
