from django.urls import path, include
from books.views import HomePage, BookListViewAPI, BookDetailViewAPI

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('api/v1/books/', BookListViewAPI.as_view(), name="book_list_api"),
    path('api/v1/books/<int:pk>/', BookDetailViewAPI.as_view(), name="book_detail_api"),
    path('api/auth/', include("rest_framework.urls")),
]