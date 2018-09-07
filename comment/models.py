from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    website = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('Post.Post', on_delete=True)  # 一篇文章有多个评论

    class Meta:
        ordering = ['-created_time']
