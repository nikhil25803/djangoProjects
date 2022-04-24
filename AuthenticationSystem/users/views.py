# from os import O_TEMPORARY
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegister
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return redirect('login')
    else:
        form = UserRegister()

    return render(request, 'register.html', {
        'form':form,
    })

@login_required
def profile(request):


    return render(request, 'profile.html')