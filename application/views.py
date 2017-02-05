# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from .models import Hospital, Account
import search


def Login(request):
	context = {}
	return render(request, 'login.html', context)

def Home(request):
	return render(request, 'landing.html', {'name': "Hospital 1"})

def Landing(request):
	name = "hsadhasd"
	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		accounts = Account.objects.all()
		for account in accounts:
			if str(account.email) == str(email) and str(account.password) == str(password):
				if str(email) == 'hospital1@email.com':
					name = 'Hospital 1'
					return render(request, 'landing.html', {'name' : name})
				else:
					name = 'Hospital 2'
					return render(request, 'landing.html', {'name' : name})
		return render(request, 'login.html', {'name': name})
	else:
		return render(request, 'login.html', {'name': name})
def View(request):
	hospitals = Hospital.objects.all()
	context = {'hospitals':hospitals}
	return render(request, 'view.html', context)

def Transfer(request):
	context = {}
	return render(request, 'transfer.html', context)

def Landing2(request):
	context = {}
	return render(request, 'landing2.html', context)

def send_case(request):
	if request.is_ajax():
		case = request.POST.get('case')
		foundH = search.search(case)
		return HttpResponse(foundH)

def send_advanced(request):
	if request.is_ajax():
		request = request.POST.get('request')
		foundH = search.search_advanced(case)
		return HttpResponse(foundH)

def send_iter(request):
	if request.is_ajax():
		request = request.POST.get('request')
		rejected = request.POST.get('rejected')
		foundH = search.search_iter(request, rejected)
		return HttpResponse(foundH)

def update_availability(request):
	if request.is_ajax():
		accepting  = request.POST.get('accepting')
		ambulance = request.POST.get('ambulance')
		hospital = request.POST.get('hospital')
		hospitals = Hospital.objects.all()
		for Hospital in hospitals:
			if Hospital.hospital_name == hospitals:
				Hospital.availability = accepting
				Hospital.ambulance = ambulance
				Hospital.save()
		return HttpResponse()

def update_availability_advanced(request):
	if request.is_ajax():
		accepting  = request.POST.get('accepting')
		ambulance = request.POST.get('ambulance')
		cases = request.POST.get('cases')
		hospital = request.POST.get('hospital')
		hospitals = Hospital.objects.all()
		for Hospital in hospitals:
			if Hospital.hospital_name == hospitals:
				Hospital.availability = accepting
				Hospital.ambulance = ambulance
				Hospital.cases = cases
				Hospital.save()
		return HttpResponse()


# def add_to_queue(request):
# 	if request.is_ajax():
# 		origin  = request.POST.get('origin')
# 		destination = request.POST.get('destination')
# 		ambulance = request.POST.get('ambulance')
# 		hospitals = Hospital.objects.all()
# 		for Hospital in hospitals:
# 			if Hospital.hospital_name == origin:
# 				add_queue(origin,destination, ambulance, eta)
# 		return HttpResponse()