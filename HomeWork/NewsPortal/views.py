from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm, PostCreate


# Create your views here.

class PostList(LoginRequiredMixin, ListView):
    raise_exception = False
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

class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsPortal.add_post')
    form_class = PostCreate
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_post = 'NW'
        return super().form_valid(form)

class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsPortal.add_post')
    form_class = PostCreate
    model = Post
    template_name = 'article_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_post = 'AR'
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsPortal.change_post')
    form_class = PostCreate
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_post = 'NW'
        return super().form_valid(form)


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsPortal.change_post')
    form_class = PostCreate
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_post = 'AR'
        return super().form_valid(form)

class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsPortal.change_post')
    form_class = PostCreate
    model = Post
    template_name = 'post_edit.html'

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

class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ("NewsPortal.dlete_post")
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


