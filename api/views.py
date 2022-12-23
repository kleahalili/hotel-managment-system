from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hotel
from .serializers import HotelSerializer
from .models import Room
from .serializers import RoomSerializer
from .models import Review
from .serializers import ReviewSerializer
from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
# def something(request):
#     return HttpResponse("testing") # we need to map this view to url

@api_view(['GET', 'POST'])
def hotels(request):
    """
    List all code snippets, or create a new snippet.
    """     
    if request.method == 'GET':
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)
@api_view(['GET', 'POST'])
def rooms(request):
    """
    List all code snippets, or create a new snippet.
    """     
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer =RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def booking(request):
    """
    List all code snippets, or create a new snippet.
    """     
    if request.method == 'GET':
        booking = Booking.objects.all()
        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def review(request):
    """
    List all code snippets, or create a new snippet.
    """     
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)