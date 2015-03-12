from flask import current_app
from unittest2 import TestCase
from .layers import AppLayer


class BasicTestCase(TestCase):
    layer = AppLayer

    def test_app_exists(self):
        self.assertFalse(current_app is None)
        self.assertFalse(self.app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
