from django.conf.urls import url
from application import views
from views import *

urlpatterns = [
	url(r'^$', Hey, name = 'Hey'),


]