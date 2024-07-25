from django.db import models

# Estate Model
class Estate(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    license_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Property Model
class Property(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    block = models.CharField(max_length=10)
    unit_number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)  # (Apartment, Villa, etc.)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.block} - {self.unit_number} ({self.type})'
