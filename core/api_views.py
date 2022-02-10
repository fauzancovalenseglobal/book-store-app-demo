from .serializers import BookSerializer, AuthorSerializer, BookListSerializer
from .models import Book, Author
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class BookListAPI(APIView):

    """API View to create Book"""
    permission_classes = (AllowAny,)
    serializer_class = BookListSerializer
    def get(self, request):
        book = Book.objects.all()
        serializer = self.serializer_class(book, many=True, context={"request": request})
        return Response({
                    "data": serializer.data,
                    "status": True,
                    "code" : status.HTTP_200_OK,
                    "message" : "Successfully fetched book"
            }, status=status.HTTP_200_OK)  


class BookCreateAPI(APIView):

    """API View to create Book"""
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer

    def post(self, request):
        """POST method to Book the data"""
        serializer = self.serializer_class(data=request.data,  context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "OK", "message": "Successfully submited form", "data": serializer.data})
        else:
            return Response({"status": "FAIL", "message": "Cannot submit form", "data": serializer.errors})


class BookUpdateAPI(APIView):

    """API View to Update Book """
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer

    def put(self, request,pk):
        """Put method to Book the data"""
        book = Book.objects.filter(pk=pk).first()
        serializer = self.serializer_class(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "OK", "message": "Successfully Updated Book form", "data": serializer.data})
        else:
            return Response({"status": "FAIL", "message": "Cannot Update form", "data": serializer.errors})


class BookDeleteAPI(APIView):

    """API View to delete Book"""
    permission_classes = (AllowAny,)
    def delete(self, request, pk):
        """
        DELETE method to delete the data
        """
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({"status": "OK", "message": "Successfully deleted book", "data": []})
        except Book.DoesNotExist:
            return Response({"status": "FAIL", "message": "book not found", "data": []})


class AuthorListAPI(APIView):

    """API View to create author"""
    permission_classes = (AllowAny,)
    serializer_class = AuthorSerializer
    def get(self, request):
        author = Author.objects.all()
        serializer = self.serializer_class(author, many=True, context={"request": request})
        return Response({
                    "data": serializer.data,
                    "status": True,
                    "code" : status.HTTP_200_OK,
                    "message" : "Successfully fetched author data"
            }, status=status.HTTP_200_OK)  


class AuthorCreateAPI(APIView):

    """API View to create Author"""
    permission_classes = (AllowAny,)
    serializer_class = AuthorSerializer

    def post(self, request):
        """POST method to Author the data"""
        serializer = self.serializer_class(data=request.data,  context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "OK", "message": "Successfully submited form", "data": serializer.data})
        else:
            return Response({"status": "FAIL", "message": "Cannot submit form", "data": serializer.errors})

class AuthorUpdateAPI(APIView):

    """API View to Update Author """
    permission_classes = (AllowAny,)
    serializer_class = AuthorSerializer

    def put(self, request,pk):
        """Put method to Author the data"""
        author = Author.objects.filter(pk=pk).first()
        serializer = self.serializer_class(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "OK", "message": "Successfully Update form", "data": serializer.data})
        else:
            return Response({"status": "FAIL", "message": "Cannot Update form", "data": serializer.errors})


class AuthorDeleteAPI(APIView):

    """API View to delete Author"""
    permission_classes = (AllowAny,)
    def delete(self, request, pk):
        """
        DELETE method to delete the data
        """
        try:
            author = Author.objects.get(pk=pk)
            author.delete()
            return Response({"status": "OK", "message": "Successfully deleted Author", "data": []})
        except Author.DoesNotExist:
            return Response({"status": "FAIL", "message": "Author not found", "data": []})


