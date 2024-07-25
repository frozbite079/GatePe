from django.urls import path
from .views import *

urlpatterns = [
     path('bokingview', BookingView.as_view(), name=''),
   
]
