# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/9 下午3:25
#       @Author  : cxy =.= 
#       @File    : tasks.py
#       @Software: PyCharm
#       @Desc    : 
# --------------------------------------
from celery import shared_task
from .models import Post
from django.db.models import F

@shared_task
def add_pv(post_id):
    """
    增加页面访问量
    :return:
    """
    Post.objects.filter(id=post_id).update(views=F('views') + 1)


@shared_task
def add_uv():
    """
    增加用户访问量
    :return:
    """
    pass