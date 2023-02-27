from django.contrib import admin
from .models import Hotel,Room,Booking,Review,PhoneNumber,PhoneNumberVerification

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(PhoneNumber)
admin.site.register(PhoneNumberVerification)