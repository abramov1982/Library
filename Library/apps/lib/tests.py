from django.test import TestCase
from django.test.client import Client
# Create your tests here.


class IndexTest(TestCase):
    def test_index(self):
        c = Client()
        r = c.get('/')
        self.assertEqual(r.status_code, 200)

    def test_add_author(self):
        c = Client()
        r = c.get('add_author/')
        self.assertEqual(r.status_code, 200)
