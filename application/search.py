# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from math import sin, cos, sqrt, atan2
from .models import Hospital




def keycomp(a, b):
	return distance(a.lattitude, a.longtitude, b.lattitude, b.longtitude)
	
def compare(a, b):
	 return (keycomp(a) < keycomp(b))

def distance(lat1, lon1, lat2, lon2):
	R = 6373.0

	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
	c = 2 * atan2(sqrt(a), sqrt(1-a))
	distance = R * c

	return distance

def search_advanced(request):
	foundH = ""
	case = request.POST.get('case')
	philhealth_accredited = request.POST.get('philhealth_accredited')
	level = request.POST.get('level')
	location = request.POST.get('location')
	city = request.POST.get('city')
	longtitude = request.POST.get('longtitude')
	lattitude = request.POST.get('lattidue')

	arrHospitals = Hospital.objects.all()
	arr2Hospital = []
	for Hospital in arrHospitals:
			if case in str(Hospital.cases) and Hospital.availability==1:
					arr2Hospital.append(Hospital)
	arr2Hospital.sort(compare)
	for Hospital in arr2Hospital:
		if Hospital.philhealth_accredited==philhealth_accredited:
			if Hospital.level==level:
				if Hospital.city == city:
					return Hospital
	for Hospital in arr2Hospital:
		if Hospital.philhealth_accredited==philhealth_accredited:
			if Hospital.level==level:
				return Hospital
	for Hospital in arr2Hospital:
		if Hospital.philhealth_accredited==philhealth_accredited:
			return Hospital
	return arr2Hospital[0]

def search(case):
	foundH = ""
	arrHospitals = Hospital.objects.all()
	arr2Hospital = []
	arr2Hospital.sort(compare)
	for Hospital in arrHospitals:
			if case in str(Hospital.cases) and Hospital.availability==1:
					return Hospital
	if len(arr2Hospital) == 0:
		return foundH
	return arr2Hospital[0]

def iter_search(request, rejected):
	foundH = ""
	case = request.POST.get('case')
	philhealth_accredited = request.POST.get('philhealth_accredited')
	level = request.POST.get('level')
	location = request.POST.get('location')
	city = request.POST.get('city')
	longtitude = request.POST.get('longtitude')
	lattitude = request.POST.get('lattidue')

	arrHospitals = Hospital.objects.all()
	arr2Hospital = []
	for Hospital in arrHospitals:
			if case in str(Hospital.cases) and Hospital.availability==1:
					if Hospital in rejected:
						continue
					else:
						arr2Hospital.append(Hospital)

	arr2Hospital.sort(compare)
	for Hospital in arr2Hospital:
		if Hospital.philhealth_accredited==philhealth_accredited:
			if Hospital.level==level:
				if Hospital.city == city:
					return Hospital
	for Hospital in arr2Hospital:
		if Hospital.philhealth_accredited==philhealth_accredited:
			if Hospital.level==level:
				return Hospital
	for Hospital in arr2Hospital:
		if Hospital.philhealth_accredited==philhealth_accredited:
			return Hospital
	return arr2Hospital[0]
