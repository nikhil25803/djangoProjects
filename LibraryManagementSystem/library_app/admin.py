from django.contrib import admin
from .models import book_upload, request_book
# Register your models here.


admin.site.register(book_upload)
admin.site.register(request_book)