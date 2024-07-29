from django.urls import path
from .views import *

urlpatterns = [
     path('booking/', BookingView.as_view(), name='booking'),
   
]
