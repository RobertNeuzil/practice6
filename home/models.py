from django.db import models

class ThingsToDo(models.Model):
	entry = models.CharField(max_length=40)
	completed = models.BooleanField(default=False)
