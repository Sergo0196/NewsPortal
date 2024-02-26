from django.urls import path
from .views import PostList, PostDetail, PostSearch, NewsCreate, ArticleCreate, NewsUpdate, ArticleUpdate, NewsDelete, ArticleDelete, PostUpdate, PostDelete, subscription
from django.views.decorators.cache import cache_page
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('news/create/', NewsCreate.as_view(), name='post_create'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('subscriptions/', subscription, name='subscription'),
]