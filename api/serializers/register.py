from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
import re

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    
    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
            'email', 'first_name', 'last_name')
        extra_kwargs = {
        'first_name': {'required': True},
        'last_name': {'required': True}
        }
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs
    
    # def validate_password(self, password):
    #     if len(password) < 8:
    #         raise serializers.ValidationError('Password must be at least 8 characters long')
    
    def validate_username(self, username):
        if not any(char.isdigit() for char in username):
            raise serializers.ValidationError('Username must contain at least one number')
        if re.search(r'[^a-zA-Z0-9_ .]', username):
            raise serializers.ValidationError('Username must only include \"_\" and \".\"')
        if len(username) < 8 or len(username) > 12:
            raise serializers.ValidationError('Username must be between 8 and 12 characters long')
        return username
       
    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        
        user.is_active = False
        
        token = RefreshToken.for_user(user).access_token
        
        verification_link = f"{settings.HOST_URL}/api/verify/{token}"

        send_mail(
            'Verify your email',
            f'Click link to verify email: {verification_link}' ,
            'email@verification.com',
            [user.email],
            fail_silently=False,
        )
        
        user.save()
        return user