from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from books.models import Book
from books.serializers import BookSerializer, BaseBookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        filter_data = {}
        for param in self.request.query_params:
            if param in ['author', 'editorial', 'id']:
                filter_data[param] = self.request.query_params[param]
            else:
                filter_data[param + '__icontains'] = self.request.query_params[param]
        queryset = Book.objects.filter(**filter_data)
        return queryset

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return BookSerializer
        else:
            return BaseBookSerializer
