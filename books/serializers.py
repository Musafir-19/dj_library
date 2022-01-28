from rest_framework import serializers
from .models import Book


# на случай, если автор будет пользователем сайта

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "email"]


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(many=False, read_only=True)
    class Meta:
        model = Book
        fields = ["title", "author", "body", "year", "in_stock"]