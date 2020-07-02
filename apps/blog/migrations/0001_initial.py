# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-07-02 20:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='blog/%Y/%m', verbose_name='博客标图')),
                ('intro', models.CharField(max_length=100, verbose_name='简介')),
                ('context', models.TextField(verbose_name='内容')),
                ('read_count', models.PositiveIntegerField(verbose_name='阅读量')),
                ('comment_count', models.PositiveIntegerField(verbose_name='评论量')),
                ('like_count', models.PositiveIntegerField(verbose_name='点赞量')),
                ('blog_cls', models.SmallIntegerField(choices=[(1, '原创'), (2, '转载')], default=1, verbose_name='博文类型')),
                ('hint', models.CharField(max_length=300, verbose_name='文章备注')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogTagModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('lable', models.CharField(max_length=100, verbose_name='标题')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogTypeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='blog_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogTypeModel', verbose_name='博文分类'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo', verbose_name='创作者'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogTagModel', verbose_name='标签'),
        ),
    ]
