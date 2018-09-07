from django.shortcuts import render, redirect
from .models import Comment
from Post.models import Post
from django.urls import reverse


def submit_comment(request, pk):
    """
    处理提交的评论
    :param request:
    :return:
    """
    post = request.POST
    comment = Comment()
    comment.name = post.get("name")
    comment.email = post.get('email')
    comment.website = post.get('url')
    comment.text = post.get('comment')
    comment.post = Post.objects.get(id=pk)
    comment.save()

    return redirect(reverse('Post:detail', kwargs={"pk": pk}))
