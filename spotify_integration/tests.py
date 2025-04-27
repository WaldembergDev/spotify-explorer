from django.test import TestCase
from .views import get_token
import os

# Create your tests here.
class TokenTests(TestCase):
    def test_get_token(self):

        token_data = get_token()

        print(token_data)

        self.assertIsNotNone(token_data)
        self.assertIn('access_token', token_data)
        self.assertIn('token_type', token_data)
