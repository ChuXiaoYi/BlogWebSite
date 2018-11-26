# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2018/8/3 下午5:29
#       @Author  : cxy =.= 
#       @File    : urls.py
#       @Software: PyCharm
# --------------------------------------
from django.conf.urls import url
from . import views

app_name = 'Post'

urlpatterns = [
    url(r'^post_list/$', views.post_list, name="post_list"),
    url(r'^cate_list/$', views.category_list, name="cate_list"),
    url(r'^tag_list/$', views.tag_list, name="tag_list"),
    url(r'^achive_list/$', views.achive_list, name="achive_list"),
    url(r'^post_list/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),

]
