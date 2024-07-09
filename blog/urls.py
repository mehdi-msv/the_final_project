from django.urls import path
from blog.views import *
from django.urls import path
from blog.feeds import LatestEntriesFeed


app_name = 'blog'


urlpatterns = [
    path('',blog_view,name='main'),
    path('<int:pid>',blog_single,name='single'),
    path('category/<str:cat_name>',blog_view,name='category'),
    path('author/<str:author_user>',blog_view,name='author'),
    path('tag/<str:tag_name>',blog_view,name='tag'),
    path('search/',blog_search,name='search'),
    path("latest/feed/", LatestEntriesFeed()),
]
