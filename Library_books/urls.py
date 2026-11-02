"""
URL configuration for Library_books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('book/create', BooksCreateView.as_view()),
    path('books', BooksListView.as_view()),
    path('book/<int:pk>', BooksRetrieveView.as_view()),
    path('book/update/<int:pk>', BooksUpdateView.as_view()),
    path('book/delete/<int:pk>', BooksDeleteView.as_view()),

    path('borrow/create', BorrowCreateView.as_view()),
    path('borrows', BorrowListView.as_view()),
    path('borrow/<int:pk>', BorrowRetrieveView.as_view()),
    path('borrow/update/<int:pk>', BorrowUpdateView.as_view()),
    path('borrow/delete/<int:pk>', BorrowDeleteView.as_view()),
]
