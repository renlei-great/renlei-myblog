import re

from django.template import Library
from django.urls import reverse


register = Library()


@register.simple_tag
def base_url(url_path):
    """生成页面最上端的导航"""
    # 组织数据
    data_list = [
        {'title': '首页', 'url': reverse('user:index')},
        {'title': '博客', 'url': reverse('blog:blog')},
        {'title': '留言', 'url': "#"},
        {'title': '友链', 'url': "#"},
    ]
    ret = re.match(r'/\w+/', url_path)
    url_path = ret.group()
    for item in data_list:
        # 当前用户访问的URL：request.path_info:  /manage/4/issues/xxx/add/
        if item['url'].startswith(url_path):
            item['url'] = ''

    template_html = f'''
        <ul>
            <li><a href="{data_list[0]['url']}">{data_list[0]['title']}</a></li>
            <li><a href="{data_list[1]['url']}">{data_list[1]['title']}</a></li>
            <li><a href="{data_list[2]['url']}">{data_list[2]['title']}</a></li>
            <li><a href="{data_list[3]['url']}">{data_list[3]['title']}</a></li>
        </ul>
        '''
    return template_html
