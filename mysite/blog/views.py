from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        'page' : page
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
    if request.method == 'POST':
        # comment_form = CommentForm(data=request.POST)
        # if comment_form.is_valid():
        #     new_comment = comment_form.save(commit=False)
        #     new_comment.post = post
        #     new_comment.save()
        
        # else:
        #     comment_form = CommentForm()
        print(request.method.POST['name'])
        exit()

    
    
    
    return render(request,'single_page.html',{'post':post,
                                                # 'comments': comments,
                                                # 'new_comment': new_comment,
                                                # 'comment_form': comment_form,
                                              
                                              })