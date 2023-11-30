from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm, PostCreate


# Create your views here.

class PostList(ListView):

    model = Post
    ordering = '-date_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10



class PostDetail(DetailView):
    model = Post
    template_name = 'news_index.html'
    context_object_name = 'news'

class PostSearch(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsCreate(LoginRequiredMixin,CreateView):
    raise_exception = True
    form_class = PostCreate
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_post = 'NW'
        return super().form_valid(form)

class ArticleCreate(CreateView):
    form_class = PostCreate
    model = Post
    template_name = 'article_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_post = 'AR'
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    form_class = PostCreate
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_post = 'NW'
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    form_class = PostCreate
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_post = 'AR'
        return super().form_valid(form)

class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.category_post == 'NW':
            return obj
        else:
            raise Http404('News not found')


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.category_post == 'AR':
            return obj
        else:
            raise Http404('Article not found')


