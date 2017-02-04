# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from .models import Hospital


def Login(request):
	context = {}
	return render(request, 'login.html', context)

def Landing(request):
	context = {}
	return render(request, 'landing.html', context)

def View(request):
	hospitals = Hospital.objects.all()
	context = {'hospitals':hospitals}
	return render(request, 'view.html', context)

def Landing2(request):
	context = {}
	return render(request, 'landing2.html', context)
