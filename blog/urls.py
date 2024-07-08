from django.urls import path
from blog.views import *
from django.urls import path
from blog.feeds import LatestEntriesFeed


app_name = 'blog'


urlpatterns = [
    path('',blog_views,name='main'),
    
    
    
    path("latest/feed/", LatestEntriesFeed()),
]
