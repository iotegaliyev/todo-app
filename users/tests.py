from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User


class UserCreateViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_valid_registration(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'password': 'strongpassword'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(User.objects.filter(username='johndoe').exists())

    def test_invalid_registration(self):
        data = {
            'first_name': 'Jane',
            'username': 'janedoe',
            'password': 'short'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertFalse(User.objects.filter(username='janedoe').exists())

    def test_duplicate_registration(self):
        existing_user = User.objects.create_user(username='existinguser', first_name='Existing', password='testpass')
        data = {
            'first_name': 'Duplicate',
            'username': 'existinguser',
            'password': 'strongpass'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(User.objects.filter(username='existinguser').count(), 1)

    def test_login_after_registration(self):
        data = {
            'first_name': 'Alice',
            'username': 'alice',
            'password': 'securepassword'
        }

        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        login_data = {
            'username': 'alice',
            'password': 'securepassword'
        }
        login_response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.assertIn('access', login_response.data)
        self.assertIn('refresh', login_response.data)
