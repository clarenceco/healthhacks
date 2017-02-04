from __future__ import unicode_literals

from django.db import models


class Hospital(models.Model):
	hospital_name = models.CharField(max_length = 50)
	availability = models.BooleanField()
	ambulance = models.BooleanField()
	location = models.TextField()
	city = models.TextField()
	contactno = models.TextField()
	def __str__(self):
		return self.hospital_name


class Account(models.Model):
	email = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	def __str__(self):
		return self.email

# Create your models here.
