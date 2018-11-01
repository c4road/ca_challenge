from django.db import models

from core.models import TimestampedModel, IntegerRangeField
# Create your models here.


# Rating - must be between 1 - 5
# Title - no more than 64 chars
# Summary - no more than 10k chars
# IP Address - IP of the review submitter
# Submission date - the date the review was submitted

class Rating(TimestampedModel):

	reviewer = models.ForeignKey(
		'authentication.User', on_delete=models.CASCADE, related_name='rating'
	)
	rating = IntegerRangeField(min_value=1,max_value=5)
	title = models.CharField(db_index=True, max_length=64)
	summary = models.TextField(max_length=10000)
	ip_address = models.GenericIPAddressField()
	slug = models.SlugField(db_index=True, max_length=255, unique=True)
	# company = models.ForeignKey(
	# 	'authentication.User', on_delete=models.CASCADE, related_name='rating'
	# )


	def __str__(self):
		return self.title

