from django.urls import path
from . import views

urlpatterns = [
   path('sth/',views.something),
   path('hotels/',views.hotels)
]
