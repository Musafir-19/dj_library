from django.views.generic import ListView
from django.db.models import Q
from .models import Book


class HomePage(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'
