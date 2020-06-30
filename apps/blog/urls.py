from django.conf.urls import url

from apps.blog.views import Blog


urlpatterns = [
    url(r'^$', Blog.as_view(), name='blog'),  # 博客页展示
]
