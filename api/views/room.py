from ..models import Room
from ..serializers import RoomSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RoomList(APIView):
    """
    List all rooms
    """
    def get(self, request, format=None):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RoomDetails(APIView):
    def get(self, request, pk, format=None):
        try:
            room = Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        try:
            room = Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            room = Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        room = Room.objects.get(pk=pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)