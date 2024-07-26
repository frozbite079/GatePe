from django.urls import path
from .views import *

urlpatterns = [
     path('boking/', BookingView.as_view(), name='boking'),
   
]
