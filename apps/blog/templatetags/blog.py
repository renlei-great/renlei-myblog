import re

from django.template import Library
from django.utils.safestring import mark_safe
from django.urls import reverse


register = Library()


@register.simple_tag
def base_url(url_path):
    """生成页面最上端的导航"""
    # 组织数据
    data_list = [
        {'title': '首页', 'url': reverse('user:index'), 'class': ''},
        {'title': '博客', 'url': reverse('blog:blog'), 'class': ''},
        {'title': '留言', 'url': "#", 'class': ''},
        {'title': '友链', 'url': "#", 'class': ''},
    ]
    ret = re.match(r'/\w+/', url_path)
    url_path = ret.group()
    for item in data_list:
        # 当前用户访问的URL：request.path_info:  /manage/4/issues/xxx/add/
        if item['url'].startswith(url_path):
            item['class'] = 'current'

    template_html = f'''
        <ul>
            <li><a class="{data_list[0]['class']}" href="{data_list[0]['url']}">{data_list[0]['title']}</a></li>
            <li><a class="{data_list[1]['class']}" href="{data_list[1]['url']}">{data_list[1]['title']}</a></li>
            <li><a class="{data_list[2]['class']}" href="{data_list[2]['url']}">{data_list[2]['title']}</a></li>
            <li><a class="{data_list[3]['class']}" href="{data_list[3]['url']}">{data_list[3]['title']}</a></li>
        </ul>
        '''
    return mark_safe(template_html)


@register.simple_tag
def add_index(a, b):
    return int(a)+int(b)
