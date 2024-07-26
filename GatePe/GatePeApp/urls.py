from django.urls import path
from .views import *


urlpatterns = [
        # path('signup/', SignupView.as_view(), name='signup'),
        # path('login/', LoginView.as_view(), name='login'),
        path('users/', UserView.as_view(), name='user-list-create'),
]
