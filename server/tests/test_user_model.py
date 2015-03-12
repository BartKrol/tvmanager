from unittest2 import TestCase
from app.main.models import User


class UserModelTestCase(TestCase):
    def test_password_setter(self):
        u = User(password='Bob')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='Bob')
        with self.assertRaises(AttributeError):
            u.password()

    def test_password_verification(self):
        u = User(password='Bob')
        self.assertTrue(u.verify_password('Bob'))
        self.assertFalse(u.verify_password('Steve'))

    def test_password_salts_are_random(self):
        u = User(password='Bob')
        u2 = User(password='Bob')
        self.assertTrue(u.password_hash != u2.password_hash)
