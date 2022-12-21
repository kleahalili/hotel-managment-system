from django.db import models
from ..models import Hotel 


class Room(models.Model):
    number=models.IntegerField(null=False)
    photos=models.FileField(upload_to ='uploads/% Y/% m/% d/',blank=True,null=True)
    characteristics=models.CharField(max_length=1000)
    room_position=models.CharField(max_length=30)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.hotel.name} {self.number}"
    