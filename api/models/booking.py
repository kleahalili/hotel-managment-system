from django.db import models
from django.contrib.auth.models import User
from ..models import Room
from datetime import datetime

class Booking(models.Model):
   # date=models.DateField(null=False)
    check_in=models.DateField(null=False)
    check_out=models.DateField(null=False)
    price=models.IntegerField(null=False)
    room=models.ForeignKey(Room,related_name="bookings",on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Booking from {self.user.username} for room {self.room.number}"