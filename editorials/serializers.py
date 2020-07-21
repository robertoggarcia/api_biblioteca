from rest_framework import serializers

from editorials.models import Editorial


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ['name', 'address', 'phone', 'web', 'created_at']
