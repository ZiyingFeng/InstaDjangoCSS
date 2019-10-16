"""Insta URL Configuration

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

#才用第二种class-based views

from django.contrib import admin
from django.urls import include, path

from InstaApp.views import HelloDjango

urlpatterns = [
    path('', HelloDjango.as_view(), name = 'helloDjango'),
    #当传入是空字符串的时候，去调用 HelloDjango 里面的 as_view 的函数
    #由于 HelloDjango 继承了 TemplateView，所以相应的 as_view 方法也会被继承下来
]
