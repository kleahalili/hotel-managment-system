from ..models import PhoneNumber, PhoneNumberVerification
from ..serializers import PhoneNumberSerializer, PhoneNumberVerificationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

class PhoneNumberList(APIView):
    def get(self, request, format=None):
        numbers = PhoneNumber.objects.filter(user=request.user)
        # Request is sent to serializer context so it can get the user
        serializer = PhoneNumberSerializer(numbers, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        # Request is sent to serializer context so it can get the user
        serializer = PhoneNumberSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhoneNumberVerificationCreate(APIView):
    def post(self, request, format=None):
        # Request is sent to serializer context so it can get the user
        serializer = PhoneNumberVerificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhoneNumberVerificationVerify(APIView):
    def get(self, request, phone_id, pin, format=None):
        phone_number_verification = PhoneNumberVerification.objects.filter(phone_id=phone_id).latest('sent')
        
        if phone_number_verification.is_valid(pin):
            phone_number = PhoneNumber.objects.get(id=phone_id)
            phone_number.verified = True
            phone_number.save()
            return Response(status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)