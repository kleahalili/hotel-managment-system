from django.urls import path
from .views import BookingList, HotelList, RoomList, ReviewList, ReviewDetails , BookingDetails
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   path('bookings/', BookingList.as_view(),name="bookings"),
   path('rooms/',RoomList.as_view(),name="rooms"),
   path('hotels/',HotelList.as_view(),name="hotels"),
   path('reviews/',ReviewList.as_view(),name="reviews"),
   path('reviews/<int:pk>/', ReviewDetails.as_view()),
   path('bookings/<int:pk>/', BookingDetails.as_view())
]
