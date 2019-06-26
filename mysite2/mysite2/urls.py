"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from test1 import views as test1_views
urlpatterns = [
    url(r'^$',test1_views.home,),
    url(r'^test/$',test1_views.home1),
    url(r'^admin/', admin.site.urls),
    url(r'^test/homenext',test1_views.home1pgnext),
    url(r'^test/homeback', test1_views.home1pgback),
    url(r'^test/trtopage',test1_views.turntopage),
    url(r'^home/movie$',test1_views.movies),
    url(r'^home/movienext$',test1_views.movies_next),
    url(r'^home/movieback$',test1_views.movies_back),
    url(r'^home/movietrtopage$',test1_views.movies_turntopage),


]
