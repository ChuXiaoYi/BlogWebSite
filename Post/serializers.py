# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2018/11/23 下午6:40
#       @Author  : cxy =.= 
#       @File    : serializers.py
#       @Software: PyCharm
#       @Desc    : 
# --------------------------------------
from rest_framework import serializers
from Post.models import Post, Category, Tag


class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = (
        'id', 'title', 'body', 'created_time', 'modified_time', 'excerpt', 'category', 'tags', 'views', 'category_name')


class CateSerializer(serializers.ModelSerializer):
    post_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'post_set')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
