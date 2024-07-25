from django.urls import path
from .views import *


urlpatterns = [
    path('estates/', EstateView.as_view(), name='estate-list-create'),
    path('properties/', PropertyView.as_view(), name='property-list-create'),
]
