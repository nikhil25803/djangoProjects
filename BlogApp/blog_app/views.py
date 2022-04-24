from multiprocessing import context
from django.shortcuts import redirect, render
from . models import Post
from . forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
def home(request):

    post_form = PostForm(request.POST or None)
    
    
    if post_form.is_valid():
        post_form.save()
        return redirect('/')
        
    data = Post.objects.all()
    all_users = get_user_model().objects.all()
    context = {
        'posts':data,
        'post_form':post_form,
        'users':all_users,
    }
    return render(request, 'index.html', context)

@login_required
def post_create(request):

    post_form = PostForm(request.POST or None)
    if post_form.is_valid():
        post_form.save()
        return redirect('/')

    context = {
        'form':post_form,
    }

    return render(request, 'createpost.html', context)