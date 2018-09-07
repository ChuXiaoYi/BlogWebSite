# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2018/8/8 上午10:45
#       @Author  : cxy =.= 
#       @File    : simple_tags.py
#       @Software: PyCharm
# --------------------------------------
from django import template
from ..models import Category, Post
from comment.models import Comment

register = template.Library()


@register.simple_tag
def get_categories():
    """
    分类目录标签
    :return:
    """
    return Category.objects.all()


@register.simple_tag
def get_hottest_post():
    """
    获取最热文章
    :return:
    """
    post_list = Post.objects.all().order_by('-views')[:5]
    return post_list

@register.simple_tag()
def get_archive():
    """
    获取最新的评论
    :return:
    """
    post_list = Post.objects.dates('created_time', 'month', order='DESC')
    return post_list
