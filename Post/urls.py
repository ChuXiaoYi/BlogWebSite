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
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name="list"),
    url(r'^detail/post-(?P<pk>\d+)/$', views.detail, name="detail"),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name="archives"),
    url(r'^category/(?P<pk>\d+)/$', views.category, name='category')

]
