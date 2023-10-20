from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'news.html'
    context_object_name = 'news'

class PostDetail(DetailView):
    model = Post
    template_name = 'news_index.html'
    context_object_name = 'news'