from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.urls import reverse
from django.shortcuts import redirect





# Create your views here.
def home(request):
    posts = Post.published.all()

    
    
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    
    context = {
        'posts': posts,
        'page' : page,
    }
    return render(request,'home.html',context)


def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug=post,
                                publish__year=year,
                                publish__month=month,
                                publish__day = day
                             
                             )
    
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form = CommentForm()
    context = {
        'post':post,
        'comments': comments,
        'comment_form': comment_form 
    }
    if request.method == 'POST':
    #     if request.POST.is_valid():
                
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            context = {'post':post,
                        'comments': comments, 
                        'new_comment': new_comment,
                        'comment_form': comment_form                                              
                        
                        
                        }
            return redirect(post) # this post is a canonical url. so we are passing just this object 
                                # to redirect to a post
    else:
        comment_form = CommentForm()
            
    
    
    return render(request,'single_page.html',context)