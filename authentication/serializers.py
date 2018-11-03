from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Reviewer


class ReviewerSerializer(serializers.ModelSerializer):

	createdAt = serializers.SerializerMethodField(method_name='get_created_at')
	updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

	class Meta:

		model = Reviewer
		fields = (

			'username', 
			'email', 
			'id', 
			'createdAt',
			'updatedAt'
		)


	def get_created_at(self, instance):
		"""
		Give iso format to the update date
		"""
		return instance.created_at.isoformat()


	def get_updated_at(self, instance):
		"""
		Give iso format to the cration date
		"""
		return instance.updated_at.isoformat()


class LoginSerializer(serializers.Serializer):

	email = serializers.CharField(max_length=255)
	username = serializers.CharField(max_length=255, read_only=True)
	password = serializers.CharField(max_length=128, write_only=True)
	token = serializers.CharField(max_length=255, read_only=True)

	def validate(self, data):

		email = data.get('email', None)
		password = data.get('password', None)
		if email is None:

			raise serializers.ValidationError('An email adress is required to log in.')
		if password is None:

			raise serializers.ValidationError('A password is required to log in.')
		user = authenticate(username=email, password=password)

		if user is None:
			raise serializers.ValidationError('A user with this email and password was not found.')

		if not user.is_active:
			raise serializers.ValidationError(
				'This user has been deactivated.'
			)

		return {

			'email': user.email,
			'username': user.username,
			'token': user.token
		}


class RegistrationSerializer(serializers.ModelSerializer):

	password = serializers.CharField(

		max_length = 128,
		min_length = 8,
		write_only = True
	)
	token = serializers.CharField(max_length = 255, read_only = True)

	class Meta:

		model = Reviewer
		fields = ('__all__')

	def create(self, validated_data):

		return Reviewer.objects.create_user(**validated_data)
		

