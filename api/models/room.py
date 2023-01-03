from django.db import models
from ..models import Hotel
from datetime import date


class Room(models.Model):
    number=models.IntegerField(null=False)
    photos=models.FileField(upload_to ='uploads/% Y/% m/% d/',blank=True,null=True)
    characteristics=models.CharField(max_length=1000)
    room_position=models.CharField(max_length=30)
    hotel=models.ForeignKey(Hotel,related_name="rooms",on_delete=models.CASCADE)
    price=models.FloatField(null=False)
     
    def __str__(self):
        return f"{self.hotel.name} {self.number}"
    
    @property
    def is_available_today(self):
        for booking in self.bookings.all():
            if booking.check_in < date.today() and booking.check_out > date.today():
                return False
        return True
    
    def is_available(self, check_in, check_out):
        for booking in self.bookings.all():
            if booking.check_in < check_out and booking.check_out > check_in:
                return False
        return True
    
    class Meta:
        unique_together = (('hotel', 'number'))