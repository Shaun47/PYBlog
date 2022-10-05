from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    posts = Post.published.all()
    context = {
        'posts': posts
    }
    return render(request,'home.html',context)