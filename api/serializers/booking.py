from rest_framework import serializers
from ..models import Booking, Room
from django.db.models import Q
from datetime import date
from datetime import datetime

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=('id', 'check_in', 'check_out', 'room', 'user', 'price')
        # User field is read only so we don't have to specify it when creating a new booking
        read_only_fields=('user',)
        
    # def room_available(self, data):
    #     return Booking.objects.filter(
    #         Q(room=data['room']) & (
        
    #         Q(check_out__gte=data['check_in'],
    #           check_out__lte=data['check_out']) |

    #         Q(check_in__gte=data['check_in'],
    #           check_in__lte=data['check_out']) |

    #         Q(check_in__gte=data['check_in'],
    #           check_out__lte=data['check_out']) |

    #         Q(check_in__lte=data['check_in'],
    #           check_out__gte=data['check_out'])
            
    #         )
    #     ).exists()
    
    def validate(self, data): # Validate
        if data['check_in'] > data['check_out']:
            raise serializers.ValidationError("Check out can't be before check in")
        
        # Check if room is available
        if not data['room'].is_available(data['check_in'], data['check_out']):
            raise serializers.ValidationError("Room is not available for those dates")
        
        return data

    def validate_check_in(self, value): # Validate check in
        if value < date.today():
            raise serializers.ValidationError("You can't check in the past")
        return value
    
    def create(self, validated_data):
        user = self.context['request'].user
        # Creating the booking for the user in context
        return Booking.objects.create(**validated_data, user=user)