from django.urls import path
from .views import *

urlpatterns = [
   
    path('v/', VisitorView.as_view(), name='visitors'),
    path('v/<int:pk>/',VisitorView.as_view(), name='visitor_update'),

]
