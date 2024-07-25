from django.urls import path
from .views import *

urlpatterns = [
     path('facilityview', FacilityView.as_view(), name=''),
     path('billingview', BillingView.as_view(), name=''),
     path('membershipview', MembershipView.as_view(), name=''),
   
]
