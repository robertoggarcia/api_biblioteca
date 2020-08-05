from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from authors.models import Author
from books.models import Book
from editorials.models import Editorial


class TestAuthorViewSet(APITestCase):
    def setUp(self) -> None:
        self.url_base = 'http://127.0.0.1:8000/api/v1'
        self.author = Author.objects.create(name='Roberto', phone='312312312', email='roberto@gmail.com')
        self.author2 = Author.objects.create(name='Roberto', phone='312312312', email='roberto@gmail.com')
        self.editorial = Editorial.objects.create(name='Roberto', address='Av. Tal', phone='342423',
                                                  web='www.web.com', created_at=timezone.now(), active=True)
        self.book = Book.objects.create(title='Book 1', pub_date='2020-03-03', author=self.author,
                                        editorial=self.editorial)
        self.book2 = Book.objects.create(title='Book 1', pub_date='2020-03-03', author=self.author2,
                                         editorial=self.editorial)

    def test_books_action(self):
        url = f'{self.url_base}/authors/{self.author.id}/books/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
