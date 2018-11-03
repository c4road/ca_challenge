import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from compnaies.models import Company
from companies.serializers import CompanySerializer

class CompanyAPITests(TestCase):

	def setUp(self):

		self.create_url = reverse('companies:company-create')

	def test_create(self):

		data = json.dumps({"name":"Company 1", "email":"company_1@gmail.com", "address":"Some address"})
		response = self.client.post(self.create_url, data=data, content_type="application/json")
		company = Company.objects.get(id=response.json()['id'])
		print(company)
		# review_serializer = RegistrationSerializer(reviewer)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
