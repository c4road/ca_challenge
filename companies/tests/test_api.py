import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyAPITests(TestCase):

	def setUp(self):

		company1 = Company.objects.create(name="Some name",email="some email",address="some address")


	def test_create(self):

		data = json.dumps({"name":"Company 1", "email":"company_1@gmail.com", "address":"Some address"})
		response = self.client.post('/api/v1/company/', data=data, content_type="application/json")
		company = Company.objects.get(id=response.json()['company']['id'])
		company_serializer = CompanySerializer(company)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_update(self):

		data = json.dumps({"name":"Company 1", "email":"company_1@gmail.com", "address":"Some address"})
		url = '/api/v1/company/{}/'.format(1)
		response = self.client.put(url, data=data, content_type="application/json")
		company = Company.objects.get(id=response.json()['company']['id'])
		company_serializer = CompanySerializer(company)
		self.assertEqual(company_serializer.data, response.json()['company'])
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_retrieve(self):

		url = '/api/v1/company/{}/'.format(1)
		response = self.client.get(url, content_type="application/json")
		company = Company.objects.get(id=response.json()['company']['id'])
		company_serializer = CompanySerializer(company)
		self.assertEqual(company_serializer.data, response.json()['company'])
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_list(self):

		url = '/api/v1/company/'
		response = self.client.get(url, content_type="application/json")
		queryset = Company.objects.all()
		company_serializer = CompanySerializer(queryset, many=True)
		self.assertEqual(company_serializer.data, response.json()['companies'])
		self.assertEqual(response.status_code, status.HTTP_200_OK)



