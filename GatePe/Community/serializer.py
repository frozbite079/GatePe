from rest_framework import serializers
from .models import *
from GatePeApp.serializer import *
from Estates.serializer import *




class CommunityPostSerializer(serializers.ModelSerializer):
    # user=UserSerializer(many=False)
    
    class Meta:
        model=CommunityPost
        fields=('user','title','content')


class NoticeSerializer(serializers.ModelSerializer):
        # estate=EstateSerializer(many=False)
        class Meta:
            model=Notice
            fields=('estate','title','content')


class SurveySerializer(serializers.ModelSerializer):
        # estate=EstateSerializer(many=False)
       
        class Meta:
            model=Survey
            fields=('estate','title','questions')


class SurveyResponseSerializer(serializers.ModelSerializer):
        # user=UserSerializer(many=False)
        # survey=SurveySerializer(many=False)
       
        class Meta:
            model=SurveyResponse
            fields=('survey','user','responses')



class FeedbackSerializer(serializers.ModelSerializer):
        # user=UserSerializer(many=False)
       
        class Meta:
            model=Feedback
            fields=('user','content')