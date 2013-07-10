# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import CalendarItem

def list(request):
	list_items = CalendarItem.objects.all()
	return render_to_response("list.html", {'list_items': list_items})