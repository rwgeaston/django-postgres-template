from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient


class ThingTest(TestCase):
    endpoint = '/api/v1/things/'

    def setUp(self):
        self.maxDiff = None
        self.client = APIClient()

    def test_things(self):
        response = self.client.get(self.endpoint)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'count': 0, 'next': None, 'previous': None, 'results': []}
        )

        response = self.client.post(
            self.endpoint,
            data={'name': 'Good Thing'}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {'id': 1, 'name': 'Good Thing'}
        )

        response = self.client.get(self.endpoint)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [{'id': 1, 'name': 'Good Thing'}]}
        )
