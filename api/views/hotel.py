from ..models import Hotel
from ..serializers import HotelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HotelList(APIView):
    """
    List all hotels
    """
    def get(self, request, format=None):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)
    
    
    
    