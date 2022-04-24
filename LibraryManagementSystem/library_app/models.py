
from cProfile import label
from pyexpat import model
from tkinter import Widget
from django import forms
from django.db import models
from django.forms import TextInput, NumberInput, EmailInput
import datetime

# Create your models here.
class book_upload(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    pages = models.IntegerField()
    languages = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self):

        return self.title

class request_book(models.Model):

    name = models.CharField(max_length=100)
    number = models.CharField(max_length=12)
    email = models.EmailField()
    book = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_link = models.CharField(max_length=100, null=True)
    date = models.DateField(("Date"), default=datetime.date.today)


    def __str__(self):

        return f"{self.book} by {self.name}"