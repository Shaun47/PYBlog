from django.contrib import admin
from django.urls import path,include
from . import views


app_name = 'blog'

urlpatterns = [
    path('',views.home,name='post_list'),
    path('tag/<slug:tag_slug>/', views.home, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail,name="post_detail"),
    # path('/comment',views.comment, name="comment")
]