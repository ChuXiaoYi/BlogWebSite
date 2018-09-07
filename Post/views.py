from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, Category
from comment.models import Comment
import markdown

def index(request):
    """
    主页
    :param request:
    :return:
    """

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

    limit = 3
    paginator = Paginator(post, limit)
    page = request.GET.get('page', 1)

    result = paginator.page(page)
    context = {
        "post_list": result,
        "page": page,
    }
    return render(request=request, template_name='Post/index.html', context=context)


def detail(request, pk):
    """

    :param request:
    :param pk: 接收到的文章的主键id
    :return:
    """
    post = Post.objects.get(id=pk)
    post.add_views()
    post.body = markdown.markdown(
        post.body,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )

    comment_list = Comment.objects.filter(post__id=pk)

    context = {
        'post': post,
        'comment_list': comment_list
    }
    return render(request, template_name='Post/single.html', context=context)
