"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^reg', views.register),                           # 注册
    re_path('login', views.login),                             # 登陆
    re_path('', views.index),                             # 主页
    re_path('^pc-geetest/register', views.get_geetest),      # 极验滑动验证码 获取验证码的url
]
