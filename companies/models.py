from django.db import models

from core.models import TimestampedModel

class Company(TimestampedModel):

	name = models.CharField(db_index=True, max_length=64)
	email = models.EmailField(db_index=True, unique=True)
	address = models.TextField(max_length=1000)


	def __str__(self):
		return self.name
