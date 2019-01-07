# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/7 下午3:01
#       @Author  : cxy =.= 
#       @File    : tasks.py
#       @Software: PyCharm
#       @Desc    : 
# --------------------------------------
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def async_send_mail(email, text, post_pk):
    """
    异步发送信息，告知被回复者有人评论
    :param email:
    :param text:
    :return:
    """
    title = "邮箱发送test"
    msg = "收到回复：" + text + \
          "\n跳转到www.chuxiaoyi.cn/detail/post-{}/查看".format(post_pk)
    from_email = settings.EMAIL_HOST_USER
    recievers = [email, ]
    print(email)
    send_mail(title, msg, from_email, recievers, fail_silently=False)
