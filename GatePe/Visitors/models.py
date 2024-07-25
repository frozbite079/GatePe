from django.db import models

from django.db import models

# Visitor Model
class Visitor(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    location = models.CharField(max_length=250)
    reason_for_visit = models.CharField(max_length=255)
    approval_status = models.CharField(max_length=50)  # (Pending, Approved, Rejected)
    visit_time = models.DateTimeField()
    security_personnel = models.ForeignKey('Residents.User', on_delete=models.SET_NULL, null=True, related_name='security_visitors')
    resident = models.ForeignKey('Residents.Resident', on_delete=models.SET_NULL, null=True, related_name='visitors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
