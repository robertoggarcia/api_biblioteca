from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_created=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
