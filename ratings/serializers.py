from rest_framework import serializers

from .models import Rating


from authentication.serializers import UserSerializer
from companies.serializers import CompanySerializer


class RatingSerializer(serializers.ModelSerializer):
	
	reviewer = UserSerializer(read_only=True)

	company = CompanySerializer(read_only=True)
	

	createdAt = serializers.SerializerMethodField(method_name='get_created_at')
	updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

	class Meta:


		model = Rating
		fields = (

			'reviewer',
			'rating',
			'title',
			'summary',
			'ip_address',
			'createdAt',
			'updatedAt'


		)

	def create(self, validated_data):
		reviewer = self.context.get('reviewer', None)

		rating = Rating.objects.create(reviewer=reviewer, **validated_data)

		return rating

	def get_created_at(self, instance):

		return instance.created_at.isoformat()


	def get_updated_at(self, instance):

		return instance.updated_at.isoformat()

