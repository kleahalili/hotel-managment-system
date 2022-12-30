from ..models import Booking, Room
from ..serializers import BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

class BookingList(APIView):
    """
    List all bookings
    """
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        bookings = Booking.objects.filter(user=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        if request.data.get('user') != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookingDetails(APIView):
    def get(self, request, pk, format=None):
        if Booking.objects.get(pk=pk).user.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        try:
            booking = Booking.objects.get(pk=pk)
            serializer = BookingSerializer(booking)
            return Response(serializer.data)
        except Booking.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        if Booking.objects.get(pk=pk).user.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        if Booking.objects.get(pk=pk).user.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        booking = Booking.objects.get(pk=pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    