from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id', 'username', 'password', 'email', 'is_staff', 'is_active', 'first_name', 'last_name')
        read_only_fields=('is_staff', "is_active")
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long')
        return password
        
        
    def validate_username(self, username):
        if not any(char.isdigit() for char in username):
            raise serializers.ValidationError('Username must contain at least one number')
        if re.search(r'[^a-zA-Z0-9_ .]', username):
            raise serializers.ValidationError('Username must only include \"_\" and \".\"')
        if len(username) < 8 or len(username) > 12:
            raise serializers.ValidationError('Username must be between 8 and 12 characters long')
        return username

    def update(self, instance, validated_data):
       
        try:
            validated_data['password'] = (make_password(validated_data["password"]))
        except:
            print("password validation failed")
        try:
            validated_data['username'] = (validated_data["username"])
        except:
            print("username validation failed")

        return super().update(instance, validated_data)

    