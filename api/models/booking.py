from django.db import models
from django.contrib.auth.models import User
from ..models import Room

class Booking(models.Model):
    date=models.DateField(null=False)
    price=models.IntegerField(null=False)
    is_available=models.BooleanField()
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)