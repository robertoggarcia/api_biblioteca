from django.db import models
from django.utils import timezone


class Editorial(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)
    web = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_created=timezone.now)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
