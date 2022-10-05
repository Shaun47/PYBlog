from django.contrib import admin
from django.urls import path,include
from . import views


app_name = 'blog'

urlpatterns = [
    path('',views.home,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail,name="post_detail")
]