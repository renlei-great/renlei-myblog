from django.shortcuts import render
from django.views import View

from blog.models import BlogModel
from utils.pagination import Pagination
from blog.forms import BlogAddForm

# Create your views here.


class Blog(View):
    """博客页"""
    def get(self, request):
        """显示"""
        # 查询所有的博客
        blogs = BlogModel.objects.all()

        # 分页
        page_object = Pagination(
            current_page=request.GET.get('page'),
            all_count=blogs.count(),
            base_url=request.path_info,
            query_params=request.GET,
            per_page=1,
        )
        blog_object_list = blogs[page_object.start:page_object.end]

        # 组织上下文
        context = {
            'blog_object_list': blog_object_list,
            'page_html': page_object.page_html(),
        }

        return render(request, 'article.html', context)


class AddBlog(View):
    def get(self, request):
        """显示添加"""
        form = BlogAddForm()

        return render(request, 'write_blog.html', {'form': form})

    def post(self, request):
        """添加博客"""
        pass
