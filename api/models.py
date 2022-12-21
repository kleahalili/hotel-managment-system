# from django.db import models
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import User



    
# class Room(models.Model):
#     number=models.IntegerField(null=False)
#     photos=models.FileField(upload_to ='uploads/% Y/% m/% d/',blank=True,null=True)
#     characteristics=models.CharField(max_length=1000)
#     room_position=models.CharField(max_length=30)
#     hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return f"{self.hotel.name} {self.number}"
    
    
    
# class Booking(models.Model):
#     date=models.DateField(null=False)
#     price=models.IntegerField(null=False)
#     is_available=models.BooleanField()
#     room=models.ForeignKey(Room,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
    
 
    


    

# class Review(models.Model):
#     CHOICES=(
#         (1, "1 star"),
#         (2, "2 stars"),
#         (3, "3 stars"),
#         (4, "4 stars"),
#         (5, "5 stars")
#     )
#     comment=models.CharField(max_length=200)
#     stars=models.IntegerField(choices = CHOICES)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    

    
    
    

    
    
    
