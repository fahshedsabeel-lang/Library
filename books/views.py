from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from books.models import Books, Borrow
from books.serializers import BookSerializer, BorrowSerializer


class BooksCreateView(CreateAPIView):
    queryset=Books.objects.all()
    serializer_class=BookSerializer


class BooksListView(ListAPIView):
    queryset=Books.objects.all()
    serializer_class=BookSerializer


class BooksRetrieveView(RetrieveAPIView):
    queryset=Books.objects.all()
    serializer_class=BookSerializer


class BooksUpdateView(UpdateAPIView):
    queryset=Books.objects.all()
    serializer_class=BookSerializer


class BooksDeleteView(DestroyAPIView):
    queryset=Books.objects.all()
    serializer_class=BookSerializer



class BorrowCreateView(CreateAPIView):
    queryset=Borrow.objects.all()
    serializer_class=BorrowSerializer

class BorrowListView(ListAPIView):
    queryset=Borrow.objects.all()
    serializer_class=BorrowSerializer

class BorrowRetrieveView(RetrieveAPIView):
    queryset=Borrow.objects.all()
    serializer_class=BorrowSerializer

class BorrowUpdateView(UpdateAPIView):
    queryset=Borrow.objects.all()
    serializer_class=BorrowSerializer

class BorrowDeleteView(DestroyAPIView):
    queryset=Borrow.objects.all()
    serializer_class=BorrowSerializer