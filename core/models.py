from django.db import models

class TimestampedModel(models.Model):

	created_at = models.DateTimeField(auto_now_add=True)

	updated_at = models.DateTimeField(auto_now=True)

	class Meta:

		abstract = True

		ordering = ['-updated_at', '-created_at']


class IntegerRangeField(models.IntegerField):

    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
        
    # def formfield(self, **kwargs):
    #     defaults = {'min_value': self.min_value, 'max_value':self.max_value}
    #     defaults.update(kwargs)
    #     return super(IntegerRangeField, self).formfield(**defaults)