from django.conf.urls import url
from application import views
from views import *

urlpatterns = [
	url(r'^$', Login, name = 'Login'),
	url(r'^home/', Landing, name = 'Landing'),

]