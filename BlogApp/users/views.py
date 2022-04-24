import imp
from pickle import NONE
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from httplib2 import Authentication
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successfull")
            return redirect('/')
        messages.error(request, "Unsuccessfull Register")
    form = NewUserForm()
    return render(request=request, template_name='register.html', context={'register_form':form})

def login_request(request):

    if request.method=='POST':

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not NONE:
                login(request, user)
                messages.info(request, f"Logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid Username or Password")

        else:
            messages.error(request, 'Invalid  Request')

    form = AuthenticationForm()

    return render(request, template_name='login.html', context={'login_form':form})

@login_required
def log_out(request):
    logout(request)
    messages.info(request, f"{{user.username}} Logged Out !")
    return render(request,'logout.html')

# Create your views here.
