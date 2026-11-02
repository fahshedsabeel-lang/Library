from rest_framework import serializers
from books.models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields="__all__"

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Borrow
        fields="__all__"
        read_only_fields=["book,borrow_date,is_returned"]