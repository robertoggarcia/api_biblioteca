from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer
from editorials.models import Editorial
from editorials.serializers import EditorialSerializer


class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    @action(detail=True, methods=['GET', 'DELETE']) # api/v1/editorials/<pk>/books
    def books(self, request, pk=None):
        editorial = self.get_object()
        if request.method == 'GET':
            books = editorial.pub_books.all()
            serialized = BookSerializer(books, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        elif request.method == 'DELETE':
            Book.objects.filter(editorial=editorial).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False) # api/v1/editorials/last
    def last(self, request):
        editorials = self.get_queryset().order_by('-created_at')
        serialized = EditorialSerializer(editorials, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=False)  # api/v1/editorials/inactive
    def inactive(self, request):
        editorials = self.get_queryset().filter(active=False)
        serialized = EditorialSerializer(editorials, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
