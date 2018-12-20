from django.contrib import admin
from .models import Category, Tag, Post

admin.site.register(Tag)
admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'views')
    list_display_links = ('id', 'title')


admin.site.register(Post, PostAdmin)
