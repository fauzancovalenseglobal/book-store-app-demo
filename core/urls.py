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

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("book-list", BookView.as_view(), name="book-list"),
    path("book-add", BookCreateView.as_view(), name="book-add"),
    path("<int:pk>/book-delete", book_delete_view, name="book-delete"),
    path("author-list", AuthorView.as_view(), name="author-list"),
    path("author-add", AuthorCreateView.as_view(), name="author-add"),
    path("<int:pk>/author-delete", author_delete_view, name="author-delete"),

]
