from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from GatePeApp.models import *
from Estates.models import *



# Resident Model
class Resident(models.Model):
    RELATION_CHOICES = [
        ('mother', 'Mother'),
        ('father', 'Father'),
        ('spouse', 'Spouse'),
        ('child', 'Child'),
        ('other', 'Other'),
    ]
    
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    relation = models.CharField(max_length=50, choices=RELATION_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.relation})'
    

# Service Request Model
class ServiceRequest(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)  # (Housekeeping, Maintenance, Repair, etc.)
    description = models.TextField()
    photo_attachments = models.JSONField(blank=True, null=True)  # List of photo attachments
    status = models.CharField(max_length=50)  # (Open, In Progress, Resolved)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Complaint Model
class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    photo_attachments = models.JSONField(blank=True, null=True)  # List of photo attachments
    status = models.CharField(max_length=50)  # (Open, In Progress, Resolved)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

