from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authors.models import Author
from authors.serializers import AuthorSerializer
from books.models import Book
from books.serializers import BookSerializer
from rest_framework.decorators import action


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=['GET'])
    def books(self, request, pk=None):
        if request.method == 'GET':
            author = self.get_object()
            books = Book.objects.filter(author=author)
            serialized = BookSerializer(books, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        if request.method == 'POST':
            pass

    @action(detail=False)
    def order(self, request):
        authors = Author.objects.all().order_by('name')
        serialized = AuthorSerializer(authors, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
