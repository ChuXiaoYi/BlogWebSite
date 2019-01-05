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
    comment.name = "test"
    comment.email = "test@qq.com"
    comment.text = post.get('comment')
    comment.post = Post.objects.get(id=pk)
    comment.reply_to = post.get('reply_to', 0)
    comment.root_to = post.get('root_to', 0)
    comment.reply_name = post.get('reply_name', '外星人')
    comment.save()

    return redirect(reverse('Post:detail', kwargs={"pk": pk}))
