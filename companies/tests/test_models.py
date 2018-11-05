from django.test import TestCase

from companies.models import Company


class CompanyModelTest(TestCase):


	def test_str_function(self):

		company = Company.objects.create(name="First company", email="firstcompany@gmail.com", address="Some Address")

		self.assertEqual(company.__str__(),"First company")
	