"""myforum URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from block.views import block_list

admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', block_list, name = "block_list"),
    url(r'^article/', include('article.urls')),
    url(r'^usercenter/', include('usercenter.urls')),
    # accounts login
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^comment/', include('comment.urls')),
    url(r'^message/', include('message.urls')),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]