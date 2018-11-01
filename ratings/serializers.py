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

			'id',
			'reviewer',
			'rating',
			'title',
			'summary',
			'ip_address',
			'company',
			'createdAt',
			'updatedAt'

		)

	def create(self, validated_data):
		reviewer = self.context.get('reviewer', None)
		company = self.context.get('company', None)
		ip_address = self.context.get('ip_address', None)

		rating = Rating.objects.create(reviewer=reviewer,company=company, ip_address=ip_address, **validated_data)

		return rating

	def get_created_at(self, instance):

		return instance.created_at.isoformat()


	def get_updated_at(self, instance):

		return instance.updated_at.isoformat()

	def validate(self, data):
	    """
	    Check that the start is before the stop.
	    """
	    if data['rating'] > 5 or data['rating'] < 1:
	        raise serializers.ValidationError("Not valid rating")
	    return data



