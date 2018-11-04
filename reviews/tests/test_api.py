import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import force_authenticate, APIRequestFactory
from rest_framework.test import APIClient, APITestCase

from companies.models import Company
from authentication.models import Reviewer
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from reviews.views import (

	ReviewRetrieveAPIView,
	CompanyReviewCreateAPIView,
	ReviewAdminAPIView,
	ReviewOwnerListAPIView,

)


class ReviewAPITests(TestCase):

	def setUp(self):

		self.company1 = Company.objects.create(name="Company 1",email="company_1@gmail.com",address="some address")
		self.company2 = Company.objects.create(name="Company 2",email="company_2@gmail.com",address="some address")
		self.company3 = Company.objects.create(name="Company 3",email="company_3@gmail.com",address="some address")

		self.reviewer1 = Reviewer.objects.create(username="reviewer1",email="reviewer1@gmail.com",password="12345678")
		self.reviewer2 = Reviewer.objects.create(username="reviewer2",email="reviewer2@gmail.com",password="12345678")


		# self.client.credentials(
  #           HTTP_AUTHORIZATION='Token ' + self.reviewer1.token)


	def test_create(self):


		# self.company1 = Company.objects.create(name="Company 1",email="company_1@gmail.com",address="some address")

		# factory = APIRequestFactory()
		# view = CompanyReviewCreateAPIView.as_view()
		
		# client = APIClient()
		# client.credentials(HTTP_AUTHORIZATION='Token ' + self.reviewer1.token)
		data = json.dumps({"review":{"rating":3, "title":"New rating", "summary":"Some summary"}})
		company_id = 1
		url = 'company/{}/create-review/'.format(company_id)
		response = self.client.post(url, data=data ,content_type='application/json')
		response.render()
		print(response.content)
		# review = Review.objects.get(pk=response.json()["id"])
		
		# request = factory.post(url, data=data ,content_type='application/json')
		# force_authenticate(request, user=self.reviewer1, token=self.reviewer1.token)
		# response = view(request)
		# print(response.render())
		
		# company = Company.objects.get(id=response.json()['company']['id'])
		# company_serializer = CompanySerializer(company)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	# def test_update(self):

	# 	data = json.dumps({"name":"Company 1", "email":"company_1@gmail.com", "address":"Some address"})
	# 	url = '/api/v1/company/{}/'.format(1)
	# 	response = self.client.put(url, data=data, content_type="application/json")
	# 	company = Company.objects.get(id=response.json()['company']['id'])
	# 	company_serializer = CompanySerializer(company)
	# 	self.assertEqual(company_serializer.data, response.json()['company'])
	# 	self.assertEqual(response.status_code, status.HTTP_200_OK)


	# def test_retrieve(self):

	# 	url = '/api/v1/company/{}/'.format(1)
	# 	response = self.client.get(url, content_type="application/json")
	# 	company = Company.objects.get(id=response.json()['company']['id'])
	# 	company_serializer = CompanySerializer(company)
	# 	self.assertEqual(company_serializer.data, response.json()['company'])
	# 	self.assertEqual(response.status_code, status.HTTP_200_OK)

	# def test_list(self):

	# 	url = '/api/v1/company/'
	# 	response = self.client.get(url, content_type="application/json")
	# 	queryset = Company.objects.all()
	# 	company_serializer = CompanySerializer(queryset, many=True)
	# 	self.assertEqual(company_serializer.data, response.json()['companies'])
	# 	self.assertEqual(response.status_code, status.HTTP_200_OK)



