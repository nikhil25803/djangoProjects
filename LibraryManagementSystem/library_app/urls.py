from tkinter import N
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('books/', views.books, name='books-page'),
    path('librarian/', views.librarian, name='librarian'),
    path('exclusive/', views.exclusive_book, name='exclusive'),
]