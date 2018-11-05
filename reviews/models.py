from django.db import models

from core.models import TimestampedModel
from companies.models import Company



class Review(TimestampedModel):

	reviewer = models.ForeignKey(

		'authentication.Reviewer', 
		on_delete=models.DO_NOTHING, 
		related_name='rating'
	)
	rating = models.PositiveSmallIntegerField()
	title = models.CharField(db_index=True, max_length=64)
	summary = models.TextField(max_length=10000)
	ip_address = models.GenericIPAddressField(blank=True, null=True)
	company = models.ForeignKey(

		'companies.Company', 
		on_delete=models.DO_NOTHING, 
		related_name='rating', 
		default=''
	)

	class Meta:

		verbose_name = "Review"
		verbose_name_plural = "Reviews"


	def __str__(self):

		return "{} {}".format(self.title,self.created_at.strftime('%d-%m-%Y'))


