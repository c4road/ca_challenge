from django.db import models

from core.models import TimestampedModel, IntegerRangeField
from companies.models import Company
# Create your models here.


class Rating(TimestampedModel):

	reviewer = models.ForeignKey(
		'authentication.User', on_delete=models.CASCADE, related_name='rating'
	)
	# rating = IntegerRangeField(min_value=1,max_value=5)
	rating = models.PositiveSmallIntegerField()
	title = models.CharField(db_index=True, max_length=64)
	summary = models.TextField(max_length=10000)
	ip_address = models.GenericIPAddressField(blank=True, null=True)
	company = models.ForeignKey(
		'companies.Company', on_delete=models.CASCADE, related_name='rating', default=''
	)


	def __str__(self):
		return self.title

