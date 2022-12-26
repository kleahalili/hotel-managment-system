from django.db import models
from ..models import Hotel
from datetime import date


class Room(models.Model):
    number=models.IntegerField(null=False)
    photos=models.FileField(upload_to ='uploads/% Y/% m/% d/',blank=True,null=True)
    characteristics=models.CharField(max_length=1000)
    room_position=models.CharField(max_length=30)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.hotel.name} {self.number}"
    
    @property
    def is_available_today(self):
        for booking in self.booking_set.all():
            if booking.check_in < date.today() and booking.check_out > date.today():
                return False
        return True

    # def check_availability(room,check_in,check_out):
    #     available_list = []
    #     booking_list = self.booking_set.all()
    #     for booking in booking_list:
    #         if booking.check_in > check_out or booking.check_out < check_in:
    #             available_list.append(True)
    #         else:
    #             available_list.append(False)

    #     return all(available_list)