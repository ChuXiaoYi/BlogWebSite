from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    website = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('Post.Post', on_delete=True)  # 一篇文章有多个评论

    # 评论
    reply_to = models.IntegerField(verbose_name="回复的哪条评论", default=0)
    reply_name = models.CharField(verbose_name="回复的哪个人", max_length=50, default=None)
    reply_email = models.EmailField(verbose_name="被回复的邮箱", max_length=50, default='chuxiaoyi@chuxiaoyi@cn')
    root_to = models.IntegerField(verbose_name="回复的是哪个主评论", default=0)

    class Meta:
        ordering = ['-created_time']
