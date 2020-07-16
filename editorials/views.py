from rest_framework import viewsets

from editorials.models import Editorial
from editorials.serializers import EditorialSerializer


class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
