from django.db import models


class Editorial(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)
    web = models.CharField(max_length=50)

    def __str__(self):
        return self.name
