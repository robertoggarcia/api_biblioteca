from django.db import models

from authors.models import Author
from core.models import BaseModel
from editorials.models import Editorial


class Book(BaseModel):
    title = models.CharField(max_length=300)
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', null=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='pub_books')

    def __str__(self):
        return self.title
