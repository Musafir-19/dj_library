from django.views.generic import ListView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Book
from .serializers import BookSerializer


class HomePage(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'


class BookListViewAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = (AllowAny,)             право доступа


class BookDetailViewAPI(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

