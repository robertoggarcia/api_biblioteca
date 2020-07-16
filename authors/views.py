from rest_framework import viewsets

from authors.models import Author
from authors.serializers import AuthorSerializer
from core.paginations import StandardResultsSetPagination


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = StandardResultsSetPagination
