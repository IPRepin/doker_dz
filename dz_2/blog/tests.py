from django.test import TestCase
from rest_framework.test import APIClient


class TestSampleView(TestCase):
    def test_view_200(self):
        url = '/admin/'
        client = APIClient()
        responce = client.get(url)
        self.assertEqual(responce.status_code, 200)

# Create your tests here