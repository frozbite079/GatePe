from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from GatePeApp.models import *
from Estates.models import *
from Facilities.models import *

# Booking Model
class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    duration = models.IntegerField()  # Duration in minutes
    payment_status = models.CharField(max_length=50)
    qr_code = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50)  # (Pending, Confirmed, Cancelled, etc.)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
