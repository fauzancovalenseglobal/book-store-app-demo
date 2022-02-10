from unicodedata import name
from django.urls import path
from .views import (
    IndexView,
    BookCreateView,
    book_delete_view,
    author_delete_view,
    BookView,
    AuthorView,
    AuthorCreateView,
)

from .api_views import (
    BookListAPI,
    BookCreateAPI,
    AuthorCreateAPI,
    AuthorListAPI,
    BookDeleteAPI,
    AuthorDeleteAPI,
    AuthorUpdateAPI,
    BookUpdateAPI
)

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("book-list", BookView.as_view(), name="book-list"),
    path("book-add", BookCreateView.as_view(), name="book-add"),
    path("<int:pk>/book-delete", book_delete_view, name="book-delete"),
    path("author-list", AuthorView.as_view(), name="author-list"),
    path("author-add", AuthorCreateView.as_view(), name="author-add"),
    path("<int:pk>/author-delete", author_delete_view, name="author-delete"),
    path("api/v1/book-list", BookListAPI.as_view(), name="book-list-api"),
    path("api/v1/book-add", BookCreateAPI.as_view(), name="book-add-api"),
    path("api/v1/author-list", AuthorListAPI.as_view(), name="book-author-api"),
    path("api/v1/author-add", AuthorCreateAPI.as_view(), name="book-author-api"),
    path("api/v1/book-delete/<int:pk>", BookDeleteAPI.as_view(), name="book-delete-api"),
    path("api/v1/author-delete/<int:pk>", AuthorDeleteAPI.as_view(), name="author-delete-api"),
    path("api/v1/author-update/<int:pk>", AuthorUpdateAPI.as_view(), name="author-update-api"),
    path("api/v1/book-update/<int:pk>", BookUpdateAPI.as_view(), name="book-update-api"),


]
