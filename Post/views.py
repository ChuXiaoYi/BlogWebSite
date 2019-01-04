from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, Category
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from comment.models import Comment
import markdown


def index(request):
    """
    主页
    :param request:
    :return:
    """
    return render(request=request, template_name='Post/index.html')


def list(request):
    post = Post.objects.all()
    for p in post:
        p.body = markdown.markdown(
            p.body,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                'markdown.extensions.fenced_code',
            ]
        )

    limit = 5
    paginator = Paginator(post, limit)
    page = request.GET.get('page', 1)
    result = paginator.page(page)
    context = {
        "post_list": result,
        "page": page,
    }
    return render(request=request, template_name='Post/list.html', context=context)


def detail(request, pk):
    """

    :param request:
    :param pk: 接收到的文章的主键id
    :return:
    """
    post = Post.objects.get(id=pk)
    post.add_views()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)

    comment_list = Comment.objects.filter(post__id=pk)
    for comment in comment_list:
        comment.text = markdown.markdown(
            comment.text,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.fenced_code',
            ]
        )

    context = {
        'post': post,
        'toc': md.toc,
        'comment_list': comment_list
    }
    return render(request, template_name='Post/single.html', context=context)


def archives(request, year, month):
    """
    按归档搜索
    :param request:
    :param year:
    :param month:
    :return:
    """
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    limit = 5
    paginator = Paginator(post_list, limit)
    page = request.GET.get('page', 1)
    result = paginator.page(page)
    context = {
        "post_list": result,
        "page": page,
    }
    return render(request, template_name='Post/index.html', context=context)


def category(request, pk):
    post_list = Post.objects.filter(category_id=pk)
    limit = 5
    paginator = Paginator(post_list, limit)
    page = request.GET.get('page', 1)
    result = paginator.page(page)
    context = {
        "post_list": result,
        "page": page,
    }
    return render(request, template_name='Post/list.html', context=context)
