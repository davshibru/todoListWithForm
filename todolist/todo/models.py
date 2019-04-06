from django.db import models
from django.conf import settings

class TodoMod(models.Model):
	action = models.CharField(max_length=70)
	CHOISE = (('doing','doing'),('done','done'),('cancer','cancer'))
	status = models.CharField(
		max_length=20, 
		choices=CHOISE,
		default='doing',
		)

	def __str__(self):
		return self.action

# Create your models here.
