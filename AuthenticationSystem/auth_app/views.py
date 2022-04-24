import re
from django.shortcuts import render
from . import views
# Create your views here.

def home(request):

    return render(request, 'index.html')
