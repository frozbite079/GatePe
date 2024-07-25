from django.urls import path
from .views import *
urlpatterns = [
    path('community_post/', CommunityPostView.as_view(), name='community_post'),
    path('notice/', NoticeView.as_view(), name='notice'),
    path('survey/', SurveyView.as_view(), name='survey'),
    path('survey_response/', SurveyResponseView.as_view(), name='survey_response'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
   
   
]
