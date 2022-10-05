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


def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug=post,
                                publish__year=year,
                                publish__month=month,
                                publish__day = day
                             
                             )
    
    
    return render(request,'single_page.html',{'post':post})