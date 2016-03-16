from django.conf.urls import url, include
from .import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^comittee/$', views.comittee, name='comittee'),
	url(r'^ownerslist/$', views.ownerslist, name='ownerslist'),
	
]