"""
URL configuration for Cia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from Cia import settings
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('captcha/', include('captcha.urls')),
    path('account/',include('allauth.urls')),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",),
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [  
                    path("__debug__/", include("debug_toolbar.urls")),
    ]

#  COMINGSOON
if settings.COMINGSOON:
    urlpatterns.insert(
            0, re_path(r"^", TemplateView.as_view(template_name="comingsoon.html"))
        )



handler400 = "Cia.error_views.error_400"     # bad request
handler403 = "Cia.error_views.error_403"     # permission denied
handler404 = "Cia.error_views.error_404"     # page not found
handler500 = "Cia.error_views.error_500"     # server error