from rest_framework import serializers

from authentication.serializers import ReviewerSerializer
from companies.serializers import CompanySerializer

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
	
	reviewer = ReviewerSerializer(read_only=True)
	company = CompanySerializer(read_only=True)
	createdAt = serializers.SerializerMethodField(method_name='get_created_at')
	updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

	class Meta:

		model = Review
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
		"""
		Creates a new Review instance 

		"""
		reviewer = self.context.get('reviewer', None)
		company = self.context.get('company', None)
		ip_address = self.context.get('ip_address', None)
		rating = Review.objects.create(reviewer=reviewer,company=company, ip_address=ip_address, **validated_data)
		return rating

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

	def validate(self, data):
	    """
	    Checks that rating is between 1 and 5
	    """
	    if data['rating'] > 5 or data['rating'] < 1:

	        raise serializers.ValidationError("Not valid rating")
	    return data



