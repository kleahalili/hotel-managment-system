from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def something(request):
    return HttpResponse("testing") # we need to map this view to url
