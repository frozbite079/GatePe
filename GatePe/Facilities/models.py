from django.db import models

from Estates.models import *

from Bookings.models import *
# Facility Model
class Facility(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    booking_slot_configuration = models.JSONField()  # Booking configuration details
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    billing = models.OneToOneField('Billing', on_delete=models.SET_NULL, null=True, blank=True, related_name='facility_detail')

    def __str__(self):
        return self.name
    
# Billing Model
class Billing(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='billings')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    payment_status = models.CharField(max_length=50)  # (Pending, Paid, Overdue)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Membership Model
class Membership(models.Model):
    MEMBERSHIP_TYPES = [
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('VIP', 'VIP'),
    ]

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, choices=MEMBERSHIP_TYPES)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} Membership in {self.estate.name}"