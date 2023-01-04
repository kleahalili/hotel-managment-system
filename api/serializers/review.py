from rest_framework import serializers
from ..models import Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Review
        fields=('__all__')
        read_only_fields=('user',)
    
    def create(self, validated_data):
        user = self.context['request'].user
        # Creating the booking for the user in context
        return Review.objects.create(**validated_data, user=user)