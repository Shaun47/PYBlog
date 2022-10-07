from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    posts = Post.published.all()
    paginator = Paginator(posts,1)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    
    context = {
        'posts': posts,
        'page' : page
    }
    return render(request,'home.html',context)


def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug=post,
                                publish__year=year,
                                publish__month=month,
                                publish__day = day
                             
                             )
    
    
    return render(request,'single_page.html',{'post':post})