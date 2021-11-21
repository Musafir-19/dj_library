from django.urls import path
from .views import SignUp

urlpatterns = [
    path('registration/', SignUp.as_view(), name='signup'),
]