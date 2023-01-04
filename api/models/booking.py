from django.db import models
from django.contrib.auth.models import User
from ..models import Room
from datetime import datetime

class Booking(models.Model):
    check_in=models.DateField(null=False)
    check_out=models.DateField(null=False)
    room=models.ForeignKey(Room,related_name="bookings",on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Booking from {self.user.username} for room {self.room.number}"
    
    def price(self):
        time_delta = self.check_out - self.check_in
        total_days = time_delta.days
        total_price = total_days * self.room.price
        return total_price