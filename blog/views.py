from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    form = PostForm()
    context = {
        "posts" : posts,
        "form" : form
    }
    return render(request, "blog/post_list.html", context)


def post_create(request):
    form = PostForm()
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Todo created successfully")
            return redirect("blog/post_list.html")
    
    context = {
        "form" : form
    }
    return render(request, "blog/post_create.html", context)