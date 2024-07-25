from django.urls import path
from .views import *

urlpatterns = [
    path('residents/', ResidentView.as_view(), name='resident-list-create'),
    path('service-requests/', ServiceRequestView.as_view(), name='service-request-list-create'),
    path('complaints/', ComplaintView.as_view(), name='complaint-list-create'),
]
