from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from authors.models import Author
from authors.serializers import AuthorSerializer
from books.models import Book
from books.serializers import BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=['GET', 'POST']) # /authors/<pk>/books/
    def books(self, request, pk=None):
        if request.method == 'GET':
            author = self.get_object() # Author.object.get(pk=pk)
            books = author.books.all() # [Book(author=author), Book(author=author)]
            serialized = BookSerializer(books, many=True)
            # [{'title':'foo', 'pub_date':'barr'},
            # {'title':'foo', 'pub_date':'barr'}]
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        elif request == 'POST':
            books_ids = request.data()
            for book_id in books_ids:
                book = Book.objects.get(id=book_id)
                book.author = self.get_object()
                book.save()
            return Response(status=status.HTTP_200_OK)
        elif request == 'DELETE':
            books_ids = request.data()
            try:
                for book_id in books_ids:
                    book = Book.objects.get(id=book_id)
                    book.author = None
                    book.save()
                return Response(status=status.HTTP_200_OK)
            except IntegrityError:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'El author no puede ser nulo'})
