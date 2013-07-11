#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calendar_app.models import CalendarItem
from django.contrib import admin

class CalendarItemAdmin(admin.ModelAdmin):
	fields = ('title', 'date', 'hour', 'description')
	list_display = ('title', 'date', 'hour')

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

	def queryset(self, request):
		qs = super(CalendarItemAdmin, self).queryset(request)
		return qs.filter(user = request.user)

admin.site.register(CalendarItem, CalendarItemAdmin)