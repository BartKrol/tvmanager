from datetime import datetime, timedelta
from flask import g
from freezegun import freeze_time
from app.auth.token import authenticate, load_user, make_payload
from .layers import DbLayer
from unittest2 import TestCase


class UserAuthenticationTest(TestCase):
    layer = DbLayer

    def test_verify_password_correct(self):
        self.assertTrue(self.user.verify_password('test'))

    def test_verify_password_incorrect(self):
        self.assertFalse(self.user.verify_password('fake'))


class TokenTest(TestCase):
    layer = DbLayer

    def test_authenticate_correct(self):
        user = authenticate(username='test@email.com', password='test')

        self.assertEqual(user, self.user)

    def test_authenticate_incorrect(self):
        user = authenticate(username='test@email.com', password='fake')
        user2 = authenticate(username='fake@email.com', password='fake')

        self.assertEqual(user, None)
        self.assertEqual(user2, None)

    @freeze_time("2000-01-01 12:00:00")
    def test_payload(self):
        payload = {
            'user_id': self.user.id,
            'exp': str(datetime.utcnow() + timedelta(seconds=300))
        }

        self.assertEqual(make_payload(self.user), payload)

    def test_load_user(self):
        user = load_user(make_payload(self.user))

        self.assertEqual(user, self.user)
        self.assertEqual(g.user, self.user)

