from django.shortcuts import render, redirect
from .models import Comment
from Post.models import Post
from django.urls import reverse

from .tasks import async_send_mail


def submit_comment(request, pk):
    """
    处理提交的评论
    :param request:
    :return:
    """
    post = request.POST
    comment = Comment()
    comment.name = post.get('comment-name', '外星人')
    comment.email = post.get('comment-email')
    comment.text = post.get('comment')
    comment.post = Post.objects.get(id=pk)
    comment.reply_to = post.get('reply_to', 0)
    comment.reply_email = post.get('reply_email', 'mail@chuxiaoyi.cn')
    comment.root_to = post.get('root_to', 0)
    comment.reply_name = post.get('reply_name', '外星人')
    comment.save()

    async_send_mail.delay(comment.reply_email, comment.text, pk)

    return redirect(reverse('Post:detail', kwargs={"pk": pk}))
