
from django.urls import path, re_path
from blog import views


urlpatterns = [
    re_path('^(\w+)/article/(\d+)/$', views.article_detail),  # 文章详情

    re_path('(\w+)/$', views.home), # home(request, username)
    # url(r'(\w+)/article/(\d+)/$', views.article_detail),  # 文章详情  article_detail(request, xiaohei, 1)

]





















