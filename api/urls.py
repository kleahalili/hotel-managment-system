from django.urls import path
from .views import (BookingList, HotelList, 
                    RoomList, RoomDetails, ReviewList, ReviewDetails , 
                    BookingDetails, Register, VerifyEmail,
                    UserList, UserDetails,
                    PhoneNumberList, PhoneNumberVerificationCreate, PhoneNumberVerificationVerify)
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .import views

urlpatterns = [
   path('bookings/', BookingList.as_view(),name="bookings"),
   path('rooms/',RoomList.as_view(),name="rooms"),
   path('rooms/<int:pk>', RoomDetails.as_view()),
   path('hotels/',HotelList.as_view(),name="hotels"),
   path('reviews/',ReviewList.as_view(),name="reviews"),
   path('reviews/<int:pk>/', ReviewDetails.as_view()),
   path('bookings/<int:pk>/', BookingDetails.as_view()), 

   # Endpoint to get jwt token
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
   path('register/', Register.as_view()),
   path('users/', UserList.as_view()),
   path('users/<int:pk>/', UserDetails.as_view()),
   path('verify/<str:token>', VerifyEmail.as_view(), name='veirfy_email'),
   
   path('phone/', PhoneNumberList.as_view()),
   path('phone-verification/', PhoneNumberVerificationCreate.as_view()),
   path('phone-verification/<str:phone_id>/<int:pin>', PhoneNumberVerificationVerify.as_view()),

]
