from django.test import TestCase


from authentication.models import Reviewer


class AuthenticationModelTest(TestCase):


	def test_register(self):

		with self.assertRaisesMessage(TypeError, 'Users must have a username.'):

				review = Reviewer.objects.create_user(username=None, password="12345678", email="username@gmail.com")

		with self.assertRaisesMessage(TypeError, 'Users must have an email adress'):

				review = Reviewer.objects.create_user(username='user_1', password="12345678", email=None)

		with self.assertRaisesMessage(TypeError, 'Superusers must have a password'):

				review = Reviewer.objects.create_superuser(username='user_1', password=None, email="username@gmail.com")

		admin = Reviewer.objects.create_superuser(username='user_1', password="12345678", email="username@gmail.com")

		self.assertEqual(admin.is_superuser, True)
		self.assertEqual(admin.is_staff, True)


		reviewer = Reviewer.objects.create_user(username="user_2", password="12345678", email="username2@gmail.com")


		self.assertEqual(reviewer.__str__(), "username2@gmail.com")
		self.assertEqual(reviewer.get_full_name(), "user_2")
		self.assertEqual(reviewer.get_short_name(), "user_2")



	