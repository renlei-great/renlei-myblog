from django.conf.urls import url

from apps.blog.views import Blog, AddBlog


urlpatterns = [
    url(r'^add/', AddBlog.as_view(), name='add_blog'),  # 博客页展示
    url(r'^', Blog.as_view(), name='blog'),  # 博客页展示

]
