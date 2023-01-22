from django.urls import path
from .views import BookingList, HotelList, RoomList, ReviewList, ReviewDetails , BookingDetails, Register, VerifyEmail
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
   path('bookings/', BookingList.as_view(),name="bookings"),
   path('rooms/',RoomList.as_view(),name="rooms"),
   path('hotels/',HotelList.as_view(),name="hotels"),
   path('reviews/',ReviewList.as_view(),name="reviews"),
   path('reviews/<int:pk>/', ReviewDetails.as_view()),
   path('bookings/<int:pk>/', BookingDetails.as_view()), 
   
   # Endpoint to get jwt token
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
   path('register/', Register.as_view()),
   path('verify/<str:token>', VerifyEmail.as_view(), name='veirfy_email'),
]
