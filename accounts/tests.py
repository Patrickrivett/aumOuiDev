from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class AuthTests(APITestCase):
    def test_signup_login_profile(self):
        # 1) Signup
        signup_url = reverse('signup')
        data = {
            "username":"bob",
            "email":"bob@example.com",
            "password":"pass123",
            "age_group":"Adult",
            "hair_types":["Oily"],
            "skin_types":["Dry"],
            "allergies":["Cats"]
        }
        resp = self.client.post(signup_url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        access = resp.data['access']

        # 2) Profile
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        profile_url = reverse('profile')
        resp = self.client.get(profile_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['username'], 'bob')
        self.assertEqual(resp.data['hair_types'], ['Oily'])
