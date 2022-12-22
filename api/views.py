from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hotel
from .serializers import HotelSerializer

# Create your views here.
def something(request):
    return HttpResponse("testing") # we need to map this view to url

@api_view(['GET', 'POST'])
def hotels(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)