from django.db import models

class CalendarItem(models.Model):
	date = models.DateField()
	hour = models.TimeField()
	title = models.CharField(max_length = 100)
	description = models.TextField()