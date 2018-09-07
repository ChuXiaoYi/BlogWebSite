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
    url(r'^index$', views.index, name="index"),
    url(r'^detail/post-(?P<pk>\d+)$', views.detail, name="detail"),


]
