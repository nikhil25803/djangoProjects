import re
from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.

class Post(models.Model):

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()
    twitter = models.CharField(max_length=100)
    dop = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.name}"