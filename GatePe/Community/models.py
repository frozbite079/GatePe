from django.db import models
from GatePeApp.models import *
from Estates.models import *


# Community Post Model
class CommunityPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Notice Model
class Notice(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# Survey Model
class Survey(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    questions = models.JSONField()  # List of survey questions
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Survey Response Model
class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    responses = models.JSONField()  # List of responses
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Feedback Model
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
