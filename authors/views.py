from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from authors.models import Author
from authors.permissions import PublicPermissions, PrivatePermissions
from authors.serializers import AuthorSerializer
from books.models import Book
from books.serializers import BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
