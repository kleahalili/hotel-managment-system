from rest_framework import serializers
from ..models import PhoneNumber, PhoneNumberVerification
from random import randint

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model=PhoneNumber
        fields=('__all__')
        read_only_fields=('user',)
        
    def create(self, validated_data):
        user = self.context['request'].user
        # Creating the phone number for the user in context
        return PhoneNumber.objects.create(**validated_data, user=user)


class PhoneNumberVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=PhoneNumberVerification
        fields=('__all__')
        read_only_fields=('sent','pin')

    def create(self, validated_data):
        pin = randint(100000, 999999)
        
        phone_number_verification = PhoneNumberVerification.objects.create(phone=validated_data['phone'], pin=pin)
       
        phone_number_verification.send_confirmation()
        
        return phone_number_verification