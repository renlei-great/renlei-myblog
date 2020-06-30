from django.db import models

from apps.user.models import UserInfo
from db.base_model import BaseModel

# Create your models here.


class BlogType(BaseModel):
    """博客分类"""
    title = models.CharField(verbose_name='标题', max_length=100)


class BlogTag(BaseModel):
    """博文标签"""
    lable = models.CharField(verbose_name='标题', max_length=100)


class Blog(BaseModel):
    """博文类"""
    title = models.CharField(verbose_name='标题', max_length=100)
    context = models.TextField(verbose_name='内容')
    tag = models.ForeignKey(verbose_name='标签', to='BlogTag')
    read_count = models.PositiveIntegerField(verbose_name='阅读量')
    comment_count = models.PositiveIntegerField(verbose_name='评论量')
    like_count = models.PositiveIntegerField(verbose_name='点赞量')
    blog_type = models.ForeignKey(verbose_name='博文分类', to='BlogType')
    BLOG_CLS_CHOICES = (
        (1, '原创'),
        (2, '转载'),
    )
    blog_cls = models.SmallIntegerField(verbose_name='博文类型', choices=BLOG_CLS_CHOICES, default=1)
    creator = models.ForeignKey(verbose_name='创作者', to='UserInfo')
    hint = models.CharField(verbose_name='文章备注', max_length=300)