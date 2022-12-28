from django.db import models
from django.contrib.auth.models import User
from ..models import Hotel
class Review(models.Model):
    CHOICES=(
        (1, "1 star"),
        (2, "2 stars"),
        (3, "3 stars"),
        (4, "4 stars"),
        (5, "5 stars")
    )
    comment=models.CharField(max_length=200)
    stars=models.IntegerField(choices = CHOICES)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,related_name="reviews",on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Review from {self.user.username} for hotel {self.hotel.name}"
    