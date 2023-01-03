from ..models import Booking, Room
from ..serializers import BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

class BookingList(APIView):
    """
    List all bookings
    """ 
    # Authentication classes removed because they are specified in settings
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        bookings = Booking.objects.filter(user=request.user)
        # Request is sent to serializer context so it can get the user
        serializer = BookingSerializer(bookings, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        # Request is sent to serializer context so it can get the user
        serializer = BookingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookingDetails(APIView):
    def get(self, request, pk, format=None):
        try:
            booking = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:            
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookingSerializer(booking)

        # Check if booking belongs to user
        if booking.user.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
    
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        try:
            booking = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:            
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Check if booking belongs to user
        if booking.user.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        serializer = BookingSerializer(booking, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            booking = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        # Check if booking belongs to user
        if booking.user.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)