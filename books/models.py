from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.TextField(verbose_name='Автор')
    body = models.TextField(verbose_name='Описание книги')
    year = models.TextField(verbose_name='Год издания')
    in_stock = models.TextField(verbose_name='Имеется в наличии')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('home')
