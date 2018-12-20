# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2018/9/18 下午4:43
#       @Author  : cxy =.= 
#       @File    : search_indexes.py
#       @Software: PyCharm
# --------------------------------------
from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()