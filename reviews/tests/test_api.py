import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from companies.models import Company
from companies.serializers import CompanySerializer
from authentication.serializers import ReviewerSerializer
from authentication.models import Reviewer
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewAPITests(TestCase):

	def setUp(self):

		self.company1 = Company.objects.create(name="Company 1",email="company_1@gmail.com",address="some address")
		self.company2 = Company.objects.create(name="Company 2",email="company_2@gmail.com",address="some address")
		self.company3 = Company.objects.create(name="Company 3",email="company_3@gmail.com",address="some address")

		self.reviewer1 = Reviewer.objects.create(username="reviewer1", email="reviewer1@gmail.com", password="12345678")
		self.reviewer2 = Reviewer.objects.create(username="reviewer2", email="reviewer2@gmail.com", password="12345678")

		self.review1 = Review.objects.create(rating=5, summary="Some summary",
		                      title="Some title",
		                      reviewer=self.reviewer1, company=self.company1)

		self.review2 = Review.objects.create(rating=5, summary="Some summary",
		                      title="Some title",
		                      reviewer=self.reviewer2, company=self.company1)

		self.review1 = Review.objects.create(rating=5, summary="Some summary",
		                      title="Some title",
		                      reviewer=self.reviewer1, company=self.company2)

		self.review1 = Review.objects.create(rating=5, summary="Some summary",
		                      title="Some title",
		                      reviewer=self.reviewer2, company=self.company2)

	def test_company_owner_review_list(self):

		url = reverse("reviews:create", kwargs={"company_id": self.company1.id })
		response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer1.token), content_type='application/json')
		queryet = Review.objects.filter(reviewer=self.reviewer1,company=self.company1)
		review_serializer = ReviewSerializer(queryet, many=True)

		self.assertEqual(review_serializer.data, response.json()['reviews'])
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_create(self):

		"""
		Tests review of first company 
		"""
		url = reverse("reviews:create", kwargs={"company_id": self.company1.id })
		data = json.dumps({"review":{"rating":3, "title":"New rating", "summary":"Some summary"}})
		reviewer = Reviewer.objects.get(username='reviewer1')
		response = self.client.post(url, data=data, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer1.token), content_type='application/json')
		review = Review.objects.get(id=response.json()['review']['id'])
		review_serializer = ReviewSerializer(review)
		company_serializer = CompanySerializer(self.company1)
		reviewer_serializer = ReviewerSerializer(self.reviewer1)

		self.assertEqual(reviewer_serializer.data, response.json()['review']['reviewer'])
		self.assertEqual(review_serializer.data, response.json()['review'])
		self.assertEqual(company_serializer.data, response.json()['review']['company'])
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		"""
		Tests review of second company 
		"""

		url = reverse("reviews:create", kwargs={"company_id": self.company2.id })
		data = json.dumps({"review":{"rating":3, "title":"New rating", "summary":"Some summary"}})
		reviewer = Reviewer.objects.get(username='reviewer1')
		response = self.client.post(url, data=data, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer1.token), content_type='application/json')
		review = Review.objects.get(id=response.json()['review']['id'])
		review_serializer = ReviewSerializer(review)
		company_serializer = CompanySerializer(self.company2)
		reviewer_serializer = ReviewerSerializer(self.reviewer1)

		self.assertEqual(reviewer_serializer.data, response.json()['review']['reviewer'])
		self.assertEqual(review_serializer.data, response.json()['review'])
		self.assertEqual(company_serializer.data, response.json()['review']['company'])
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		
		"""
		Tests review of third company and second reviewer
		"""

		url = reverse("reviews:create", kwargs={"company_id": self.company3.id })
		data = json.dumps({"review":{"rating":3, "title":"New rating", "summary":"Some summary"}})
		reviewer = Reviewer.objects.get(username='reviewer1')
		response = self.client.post(url, data=data, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer2.token), content_type='application/json')
		review = Review.objects.get(id=response.json()['review']['id'])
		review_serializer = ReviewSerializer(review)
		company_serializer = CompanySerializer(self.company3)
		reviewer_serializer = ReviewerSerializer(self.reviewer2)

		self.assertEqual(reviewer_serializer.data, response.json()['review']['reviewer'])
		self.assertEqual(review_serializer.data, response.json()['review'])
		self.assertEqual(company_serializer.data, response.json()['review']['company'])
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		"""
		Tests review of not found company
		"""
		# with self.assertRaisesMessage(Company.NotFound, 'Company matching query does not exist.'):
		url = reverse("reviews:create", kwargs={"company_id": 100 })
		data = json.dumps({"review":{"rating":3, "title":"New rating", "summary":"Some summary"}})
		reviewer = Reviewer.objects.get(username=self.reviewer2.username)
		response = self.client.post(url, data=data, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer2.token), content_type='application/json')


		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



	def test_retrieve(self):


		review = Review.objects.create(rating=1, summary="Some summary",
		                      title="mock title",
		                      reviewer=self.reviewer1, company=self.company1)
		url = reverse("reviews:retrieve", kwargs={"review_id": review.id })
		response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer1.token), content_type='application/json')
		review = Review.objects.get(id=response.json()['review']['id'])
		review_serializer = ReviewSerializer(review)
		reviewer_serializer = ReviewerSerializer(self.reviewer1)

		self.assertEqual(reviewer_serializer.data, response.json()['review']['reviewer'])
		self.assertEqual(review_serializer.data, response.json()['review'])
		self.assertEqual(response.status_code, status.HTTP_200_OK)

		"""
		Tests forbidden review if reviewer is not owner
		"""
		response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer2.token), content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_delete_owner_review(self):

		review = Review.objects.create(rating=1, summary="Some summary",
		                      title="will delete",
		                      reviewer=self.reviewer1, company=self.company1)
		url = reverse("reviews:retrieve", kwargs={"review_id": review.id })
		response = self.client.delete(url, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer1.token), content_type='application/json')

		with self.assertRaisesMessage(Review.DoesNotExist, 'Review matching query does not exist.'):

			review = Review.objects.get(title="will delete")

		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

		"""
		Tests forbidden review if reviewer is not owner
		"""
		review = Review.objects.create(rating=1, summary="Some summary",
		                      title="mock title",
		                      reviewer=self.reviewer1, company=self.company1)
		url = reverse("reviews:retrieve", kwargs={"review_id": review.id })
		response = self.client.delete(url, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer2.token), content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_update_owner_review(self):

		review = Review.objects.create(rating=1, summary="Some summary",
		                      title="will update",
		                      reviewer=self.reviewer1, company=self.company1)
		url = reverse("reviews:retrieve", kwargs={"review_id": review.id })
		data = json.dumps({"rating":5, "title":"New title updated", "summary":"Some summary updated"})
		response = self.client.put(url, data=data, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer1.token), content_type='application/json')
		review = Review.objects.get(id=review.id)
		review_serializer = ReviewSerializer(review)


		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(review_serializer.data, response.json()['review'])

		"""
		Tests forbidden review if reviewer is not owner
		"""
		review = Review.objects.create(rating=1, summary="Some summary",
		                      title="mock title",
		                      reviewer=self.reviewer1, company=self.company1)
		url = reverse("reviews:retrieve", kwargs={"review_id": review.id })
		response = self.client.delete(url, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer2.token), content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_owner_list(self):

		
		url = reverse("reviews:owner-list")
		response1 = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer1.token), content_type='application/json')
		queryset = Review.objects.filter(reviewer=self.reviewer1.id)
		review_serializer_1 = ReviewSerializer(queryset, many=True)

		self.assertEqual(response1.status_code, status.HTTP_200_OK)
		self.assertEqual(review_serializer_1.data, response1.json()['reviews'])

		"""
		Tests user just can see reviews he owns
		"""

		response2 = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer2.token), content_type='application/json')
		queryset = Review.objects.filter(reviewer=self.reviewer2.id)
		review_serializer_2 = ReviewSerializer(queryset, many=True)

		self.assertEqual(response1.status_code, status.HTTP_200_OK)
		self.assertNotEqual(response1.json()['reviews'],response2.json()['reviews'])
		self.assertNotEqual(review_serializer_1.data, review_serializer_2.data)

	def test_admin_list(self):

		url = reverse("reviews:admin-list")
		response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer1.token), content_type='application/json')

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

		reviewer = Reviewer.objects.get(id=self.reviewer1.id)

		reviewer.is_staff = True
		reviewer.save()

		response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.reviewer1.token), content_type='application/json')

		queryset = Review.objects.all()
		review_serializer = ReviewSerializer(queryset, many=True)

		self.assertEqual(review_serializer.data, response.json()['reviews'])
		self.assertEqual(response.status_code, status.HTTP_200_OK)


















