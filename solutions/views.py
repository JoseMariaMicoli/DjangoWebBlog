# Create your views here.
from solutions.models import Solution

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def solution(request):
	lista = Solution.objects.all()
	return render_to_response('solutions/solutions.html', locals(), context_instance=RequestContext(request))

