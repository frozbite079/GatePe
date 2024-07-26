from django.urls import path
from .views import *

urlpatterns = [
     path('facility/', FacilityView.as_view(), name='facility'),
     path('billing/', BillingView.as_view(), name='billing'),
     path('membership/', MembershipView.as_view(), name='membership'),
   
]
