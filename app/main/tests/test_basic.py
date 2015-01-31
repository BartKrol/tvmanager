from flask import current_app
from unittest2 import TestCase
from app import create_app


class MyTest(TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def test_app_exists(self):
        self.assertFalse(current_app is None)
        self.assertFalse(self.app is None)
