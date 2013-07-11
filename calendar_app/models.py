#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class CalendarItem(models.Model):
	title = models.CharField(max_length = 100)
	date = models.DateField()
	hour = models.TimeField()
	description = models.TextField()
	user = models.ForeignKey(User)

	def __unicode__(self):
		return u'%s - %s %s' % (self.title, self.date, self.hour)
