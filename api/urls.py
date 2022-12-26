from django.urls import path
from .views.booking import BookingList
from .views.room import RoomList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   path('bookings/', BookingList.as_view()),
   path('rooms/',RoomList.as_view())
]
