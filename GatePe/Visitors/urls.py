from django.urls import path
from .views import *

urlpatterns = [
   
    path('v/', VisitorView.as_view(), name='visitors'),
   

]
