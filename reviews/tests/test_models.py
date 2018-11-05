from django.test import TestCase
from reviews.models import Review
from authentication.models import Reviewer
from companies.models import Company


class ReviewModelTest(TestCase):


	def test_str_function(self):

		reviewer = Reviewer.objects.create_user(username="user_2", password="12345678", email="username2@gmail.com")

		company = Company.objects.create(name="First company", email="firstcompany@gmail.com", address="Some Address")

		review = Review.objects.create(
			reviewer = reviewer,
			rating = 5,
			title = "Some title",
			summary = "Some summary",
			ip_address = "0.0.0.0",
			company = company,

		)

		time = review.created_at


		self.assertEqual(review.__str__(), "Some title {}".format(time.strftime('%d-%m-%Y')))