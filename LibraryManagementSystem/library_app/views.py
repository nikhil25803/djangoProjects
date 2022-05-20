from multiprocessing import context
from django import views
from django.http import HttpResponse
from django.shortcuts import redirect, render
import json
from . forms import BookForm, RequestForm
from .models import book_upload, request_book
import pyrebase

config = {
    "apiKey": "AIzaSyDX8P_Eq_1AiHjuYI2tLGkkNh8GoKb1t44",
    "authDomain": "library-project-c5543.firebaseapp.com",
    "databaseURL":"https://library-project-c5543-default-rtdb.firebaseio.com",
    "projectId": "library-project-c5543",
    "storageBucket": "library-project-c5543.appspot.com",
    "messagingSenderId": "303980281900",
    "appId": "1:303980281900:web:4d28943aa78527aa411189",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

booksData = open('static/books.json').read()

data = json.loads(booksData)

# Create your views here.
def index(request):

    motive_data = database.child('Data').child('motive')

    request_form = RequestForm(request.POST or None)
    if request_form.is_valid():
        request_form.save()
        return redirect('/')

    context = {
        'r_form':request_form,
        'motive_data':motive_data,
    }

    return render(request, 'index.html', context)

def books(request):
    context = {'books':data}

    return render(request, 'books.html', context)

def librarian(request):

    request_data = request_book.objects.all()

    book_request_from = BookForm(request.POST or None)
    if book_request_from.is_valid():
        book_request_from.save()
        return redirect('/librarian')

    

    context = {
        'form':BookForm,
        'requests':request_data,
    }

    return render(request, 'librarian.html', context)

def exclusive_book(request):

    data = book_upload.objects.all()

    context = {
        'books': data
    }

    return render(request, 'exclusive.html', context)
