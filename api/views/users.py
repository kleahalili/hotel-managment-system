from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import permissions, authentication,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User
from ..serializers import UserSerializer

class UserList(APIView):
    permission_classes = [IsAuthenticated]

    def get(user, request, format=None):
        try:
            user = User.objects.get(id=request.user.id)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if user.is_staff:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        
        return Response(status=status.HTTP_403_FORBIDDEN)
     
class UserDetails(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(user, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if user.id != request.user.id and not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def patch(user, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if user.id != request.user.id and not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        if user.id != request.user.id and not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        User.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



