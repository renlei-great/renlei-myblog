from django.shortcuts import render
from django.views import View

# Create your views here.


class Blog(View):
    """博客页"""
    def get(self, request):
        """显示"""
        return render(request, 'article.html')
