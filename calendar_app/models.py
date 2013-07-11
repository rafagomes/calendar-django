from django.db import models

class CalendarItem(models.Model):
	title = models.CharField(max_length = 100)
	date = models.DateField()
	hour = models.TimeField()
	description = models.TextField()