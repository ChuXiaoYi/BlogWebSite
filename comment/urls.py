# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2018/8/3 下午5:29
#       @Author  : cxy =.= 
#       @File    : urls.py
#       @Software: PyCharm
# --------------------------------------
from django.conf.urls import url
from . import views

app_name = 'comment'

urlpatterns = [
    url(r'^comment/post-(?P<pk>\d+)$', views.submit_comment, name="comment"),

]
