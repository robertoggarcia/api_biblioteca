from rest_framework import serializers

from authors.serializers import BaseAuthorSerializer
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    author = BaseAuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'pub_date', 'author', 'editorial']
