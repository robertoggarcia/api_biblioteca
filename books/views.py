from datetime import datetime, timedelta

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer, BaseBookSerializer
from books.tasks import send_mail


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

    @action(detail=True)
    def send_email(self, request, pk=None):
        eta = datetime.now() + timedelta(days=30)
        send_mail.apply_async(args=['roberto@gmail.com'], eta=eta)
        return Response(status=status.HTTP_200_OK)
        # celery -A biblioteca worker -l info
