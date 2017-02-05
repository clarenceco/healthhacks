from django.conf.urls import url
from application import views
from views import *

urlpatterns = [
	url(r'^$', Login, name = 'Login'),
	url(r'^home/', Landing, name = 'Landing'),
	url(r'^view/', View, name = 'View'),
	url(r'^send_case/', View, name = 'send_case'),
	url(r'^back/', Home, name = 'Home'),
	url(r'^transfer/', Transfer, name = 'Transfer'),
]