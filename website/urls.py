from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import TemplateView
from website.views import *
app_name = 'website'


urlpatterns = [
    path('',TemplateView.as_view(template_name='website/index.html'),name='index'),
    path('about',TemplateView.as_view(template_name='website/about.html'),name='about'),
    path('coffees',TemplateView.as_view(template_name='website/coffees.html'),name='coffees'),
    path('contact',contact_view,name='contact'),
]