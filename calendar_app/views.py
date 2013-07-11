#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import CalendarItem
from forms import FormCalendarItem

def list(request):
	list_items = CalendarItem.objects.all()
	return render_to_response("list.html", {'list_items': list_items})

def add(request):
	if request.method == 'POST':
		form = FormCalendarItem(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('success.html', {})
	else:
		form = FormCalendarItem()
	return render_to_response('add.html', {'form': form}, context_instance = RequestContext(request))

def item(request, nr_item):
	item = get_object_or_404(CalendarItem, pk=nr_item)
	if request.method == 'POST':
		form = FormCalendarItem(request.POST, request.FILES, instance = item)
		if form.is_valid():
			form.save()
			return render_to_response('success.html', {})
	else:
		form = FormCalendarItem(instance = item)
	return render_to_response('item.html', {'form': form}, context_instance = RequestContext(request))