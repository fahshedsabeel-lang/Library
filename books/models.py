from django.db import models

# Create your models here.

class Books(models.Model):
    title=models.CharField(max_length=100)
    auther=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    isbn=models.CharField(max_length=100)
    available_copies=models.IntegerField()


class Borrow(models.Model):
    book = models.ForeignKey(Books, on_delete=models.PROTECT, related_name='borrows')
    borrower_name=models.CharField(max_length=100)
    borrower_email=models.EmailField()
    borrow_date=models.DateField(auto_now_add=True)
    is_returned=models.BooleanField(default=False)  