from django.urls import path
from .views import  search_page

urlpatterns = [
    path('search/', search_page, name='search'),
]