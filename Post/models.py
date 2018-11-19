from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    """分类"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    """文章"""
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=100, blank=True)  # 文章摘要，可为空
    category = models.ForeignKey(Category, on_delete=True)  # ForeignKey表示1对多（多个post对应1个category）
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)  # 阅读量

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Post:detail', kwargs={'pk': self.id})

    def add_views(self):
        """
        增加阅读量
        :return:
        """
        self.views += 1
        self.save(update_fields=['views'])
