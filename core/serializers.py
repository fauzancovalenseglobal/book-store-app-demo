from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ('id', 'title', 'authors', 'description', "created_at", "updated_at")

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ('id', 'first_name', 'last_name', 'email', "created_at", "updated_at")


class BookListSerializer(serializers.ModelSerializer):
  authors = AuthorSerializer()
  class Meta:
    model = Book
    fields = ('id', 'title', 'authors', 'description', "created_at", "updated_at")
