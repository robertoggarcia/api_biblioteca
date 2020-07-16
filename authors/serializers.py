from rest_framework import serializers

from authors.models import Author


class BaseAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'phone', 'email']
