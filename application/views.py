# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings


def Login(request):
	context = {}
	return render(request, 'login.html', context)

def Landing(request):
	context = {}
	return render(request, 'landing.html', context)

def View(request):
	context = {}
	return render(request, 'view.html', context)
