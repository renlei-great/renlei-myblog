from django.db import models

from db.base_model import BaseModel

# Create your models here.


class BlogTypeModel(BaseModel):
    """博客分类"""
    title = models.CharField(verbose_name='标题', max_length=100)


class BlogTagModel(BaseModel):
    """博文标签"""
    lable = models.CharField(verbose_name='标题', max_length=100)


class BlogModel(BaseModel):
    """博文类"""
    title = models.CharField(verbose_name='标题', max_length=100)
    image = models.ImageField(verbose_name='博客标图', null=True, blank=True, upload_to="blog/%Y/%m", max_length=100)
    intro = models.CharField(verbose_name='简介', max_length=100)
    context = models.TextField(verbose_name='内容')
    tag = models.ForeignKey(verbose_name='标签', to='BlogTagModel')
    read_count = models.PositiveIntegerField(verbose_name='阅读量')
    comment_count = models.PositiveIntegerField(verbose_name='评论量')
    like_count = models.PositiveIntegerField(verbose_name='点赞量')
    blog_type = models.ForeignKey(verbose_name='博文分类', to='BlogTypeModel')
    BLOG_CLS_CHOICES = (
        (1, '原创'),
        (2, '转载'),
    )
    blog_cls = models.SmallIntegerField(verbose_name='博文类型', choices=BLOG_CLS_CHOICES, default=1)

    creator = models.ForeignKey(verbose_name='创作者', to='user.UserInfo')
    hint = models.CharField(verbose_name='文章备注', max_length=300)