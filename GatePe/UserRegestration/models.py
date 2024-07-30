from django.db import models

class UserRegestration(models.Model):
    
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'UserRegestration'