from django.db import models

from authors.models import Author
from editorials.models import Editorial


class Book(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='pub_books')

    def __str__(self):
        return self.title
