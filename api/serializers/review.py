from rest_framework import serializers
from ..models import Review
from django.contrib.auth.models import User

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Review
        fields=('__all__')
        read_only_fields=('user',)
    
    def create(self, validated_data):
        user_id = self.context['request'].user.id
        # Creating the booking for the user in context
        return Review.objects.create(**validated_data, user=User.objects.get(pk=user_id))