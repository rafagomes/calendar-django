#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from models import CalendarItem

class FormCalendarItem(forms.ModelForm):
	class Meta:
		model = CalendarItem
		fields = ('title', 'date', 'hour', 'description')