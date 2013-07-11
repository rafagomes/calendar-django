#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from models import CalendarItem
from forms import FormCalendarItem

@login_required
def list(request):
	list_items = CalendarItem.objects.filter(user = request.user)
	return render_to_response("list.html", {'list_items': list_items}, context_instance = RequestContext(request))

@login_required
def add(request):
	if request.method == 'POST':
		form = FormCalendarItem(request.POST, request.FILES)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
			return render_to_response('success.html', {})
	else:
		form = FormCalendarItem()
	return render_to_response('add.html', {'form': form}, context_instance = RequestContext(request))

@login_required
def item(request, nr_item):
	item = get_object_or_404(CalendarItem, pk=nr_item, user = request.user)
	if request.method == 'POST':
		form = FormCalendarItem(request.POST, request.FILES, instance = item)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
			return render_to_response('success.html', {})
	else:
		form = FormCalendarItem(instance = item)
	return render_to_response('item.html', {'form': form}, context_instance = RequestContext(request))
@login_required
def remove(request, nr_item):
	item = get_object_or_404(CalendarItem, pk=nr_item, user = request.user)
	if request.method == 'POST':
		item.delete()
		return render_to_response('removed.html', {})

	return render_to_response('remove.html', {'item': item}, context_instance = RequestContext(request))