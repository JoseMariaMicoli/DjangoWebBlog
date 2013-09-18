from django.conf.urls import *
from solutions.models import Solution

urlpatterns = patterns('solutions.views',
	url(r'^$', 'solution', name='solution'),
)
