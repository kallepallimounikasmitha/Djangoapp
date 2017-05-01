"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blogg.views import Home
from blogg.views import Post,Lists,Detail
from blogg.views import Mate,List,Details
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name= 'Home'),
    url(r'^post/', Lists.as_view(), name='Post'),
    url(r'^detail/(?P<pk>[0-9]+)', Detail.as_view() ,name='detail'),
    url(r'^mate/', List.as_view(), name = 'Mate'),
    url(r'^details/(?P<pk>[0-9]+)', Details.as_view() ,name='details'),
]
