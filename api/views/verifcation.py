from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.conf import settings
from rest_framework.response import Response
import jwt
from django.contrib.auth.models import User

class VerifyEmail(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request, token, format=None):
        
        try:
        
            payload = jwt.decode(token , settings.SECRET_KEY, algorithms="HS256") 
            user = User.objects.get(id=payload["user_id"])
            

            if user.is_active:
                return Response("User already verified", status=status.HTTP_400_BAD_REQUEST)
            
            user.is_active = True
            user.save()
            
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
   