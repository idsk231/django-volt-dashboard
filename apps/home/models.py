# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


# class Tag(models.Model):
#     name = models.CharField('标签', max_length=20)
#     slug = models.SlugField(unique=True)
#     description = models.TextField('描述', max_length=240, default='日志标签',
#                                    help_text='用来作为SEO中description,长度参考SEO标准')
#
#     class Meta:
#         verbose_name = '标签'
#         verbose_name_plural = verbose_name
#         ordering = ['id']
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('blog:tag', kwargs={'slug': self.slug})
#
#     def get_log_list(self):
#         return FlightLog.objects.filter(tags=self)


class Category(models.Model):
    name = models.CharField('机型', max_length=20)
    slug = models.SlugField(unique=True)
    description = models.TextField('描述', max_length=240, default='机型',
                                   help_text='用来作为SEO中description,长度参考SEO标准')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})

    def get_log_list(self):
        return FlightLog.objects.filter(category=self)


class FlightLog(models.Model):
    title = models.CharField(max_length=150, verbose_name='标题')
    category = models.ForeignKey(Category, verbose_name='', on_delete=models.PROTECT)
    description = models.TextField('描述', max_length=230, default='文章摘要等同于网页description内容，请务必填写...')
    upload_date = models.DateTimeField(verbose_name='修改时间', auto_now_add=True)
    origin_name = models.CharField(max_length=150, verbose_name='原文件名')
    # tags = models.ManyToManyField(Tag, verbose_name='标签')
    video_url = models.CharField('视频链接', default='.', max_length=255)

    class Meta:
        verbose_name = '日志'
        verbose_name_plural = verbose_name
        ordering = ['-upload_date']

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def get_pre(self):
        return FlightLog.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):
        return FlightLog.objects.filter(id__gt=self.id).order_by('id').first()