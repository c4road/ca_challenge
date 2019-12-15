import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from authentication.models import Reviewer
from authentication.serializers import RegistrationSerializer, LoginSerializer

class AuthenticationAPITests(TestCase):

	def setUp(self):

		self.register_url = reverse('auth:register')
		self.login_url = reverse('auth:login')

	def test_register(self):

		data = json.dumps({"user":{"email":"user_4@gmail.com", "password":"12345678", "username":"user_4"}})

		response = self.client.post(self.register_url, data=data, content_type="application/json")
		reviewer = Reviewer.objects.get(id=response.json()["reviewer"]['id'])
		review_serializer = RegistrationSerializer(reviewer)
		self.assertEqual(review_serializer.data, response.json()['reviewer'])
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_login(self):

		data = json.dumps({"user":{"email":"user_4@gmail.com", "password":"12345678", "username":"user_4"}})
		register_response = self.client.post(self.register_url, data=data, content_type="application/json")
		data = json.dumps({"user":{"email":"user_4@gmail.com", "password":"12345678"}})
		login_response = self.client.post(self.login_url, data=data, content_type="application/json")

		self.assertEqual(login_response.status_code, status.HTTP_200_OK)


