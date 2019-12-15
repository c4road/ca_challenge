from django.db import models

from core.models import TimestampedModel

class Company(TimestampedModel):

	name = models.CharField(db_index=True, max_length=500)
	email = models.EmailField(db_index=True, unique=True)
	address = models.TextField(max_length=1000)

	class Meta:

	    verbose_name = "Company"
	    verbose_name_plural = "Companies"

	def __str__(self):
		
		return self.name
