from rest_framework import serializers
from .models import *
from GatePeApp.serializer import *
class CommunityPostSerializer(serializers.ModelSerializer):
       class Meta:
        model=CommunityPost
        fields=('user','title','content')