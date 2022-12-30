from rest_framework import serializers
from ..models import Booking, Room
from django.db.models import Q
from datetime import date
 
def room_available(validated_data):
    available = True
    if Booking.objects.filter(
            Q(room=validated_data['room']) & (
        
            Q(check_out__gte=validated_data['check_in'],
              check_out__lte=validated_data['check_out']) |

            Q(check_in__gte=validated_data['check_in'],
              check_in__lte=validated_data['check_out']) |

            Q(check_in__gte=validated_data['check_in'],
              check_out__lte=validated_data['check_out']) |

            Q(check_in__lte=validated_data['check_in'],
              check_out__gte=validated_data['check_out'])
            
            )
    ).exists():
        available = False

    return available

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Booking
        fields=('id', 'check_in', 'check_out', 'room', 'user', 'price')
    
    def validate(self, data): # ktu kalon all data si dictionary
        if data['check_in'] > data['check_out']:
            raise serializers.ValidationError("Check out can't be before check in")
        return data
        
    def validate_check_in(self, value): # ktu kalon vtm check_in
        if value < date.today():
            raise serializers.ValidationError("You can't check in the past")
        return value
    
    def create(self, validated_data):
        if room_available(validated_data):
            return Booking.objects.create(**validated_data)
        else:
            raise serializers.ValidationError({
                "detail": "Room is not available for these dates."
        })

    def update(self, instance, validated_data):
        if room_available(validated_data):
            instance.save()
        else:
            raise serializers.ValidationError({
                "detail": "Room is not available for these dates."
            })
        return instance