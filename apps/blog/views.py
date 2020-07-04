from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import View

from blog.models import BlogModel, BlogTypeModel
from utils.pagination import Pagination
from blog.forms import BlogAddForm
from myblog.settings import PER_PAGE_NUM

# Create your views here.


class Blog(View):
    """博客页"""
    def get(self, request):
        """显示"""
        # 查询所有的博客
        blogs = BlogModel.objects.all()

        # 分页
        per_page = PER_PAGE_NUM
        page_object = Pagination(
            current_page=request.GET.get('page', 1),
            all_count=blogs.count(),
            base_url=request.path_info,
            query_params=request.GET,
            per_page=per_page,
        )
        blog_object_list = blogs[page_object.start:page_object.end]

        # 查询出所有标签
        tag_all = BlogTypeModel.objects.all().order_by('index')

        blogs = BlogModel.objects.all()
        # 最新文章
        new_blogs = blogs.order_by('-create_time')[0:5]
        # 最热文章
        hot_blogs = blogs.order_by('-read_count')[0:3]

        # 组织上下文
        context = {
            'blog_object_list': blog_object_list,
            'page_html': page_object.page_html(),
            'tag_all': tag_all,
            'new_blogs': new_blogs,
            'hot_blogs': hot_blogs,
        }

        return render(request, 'article.html', context)


class AddBlog(View):
    def get(self, request):
        """显示添加"""
        form = BlogAddForm()

        return render(request, 'write_blog.html', {'form': form})

    def post(self, request):
        """添加博客"""
        a = request.POST
        print(request.POST)
        blog_form = BlogAddForm(request.POST)
        blog_form.save()
        return redirect(reverse('blog:blog'))
