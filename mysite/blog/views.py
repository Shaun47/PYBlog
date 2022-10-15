from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.urls import reverse
from django.shortcuts import redirect
from taggit.models import Tag





# Create your views here.
def home(request, tag_slug=None):
    posts = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in = [tag])
    
    
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
        'tag'  : tag, 
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
            
    post_tags_ids = post.tags.values_list('id',flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    context = {
        'post':post,
        'comments': comments,
        'comment_form': comment_form, 
        'similar_posts': similar_posts,
    }
    
    return render(request,'single_page.html',context)