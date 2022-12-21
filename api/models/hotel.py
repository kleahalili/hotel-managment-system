from django.db import models


class Hotel(models.Model):
    
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=40)
    city=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    