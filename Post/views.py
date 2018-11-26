from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Post.models import Post, Category, Tag
from Post.serializers import PostSerializer, CateSerializer, TagSerializer
import markdown


@csrf_exempt
def post_detail(request, pk):
    if request.method == 'GET':
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        response = JsonResponse(serializer.data, safe=True)
        response['Access-Control-Allow-Origin'] = "*"
        return response


@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        for p in posts:
            p.body = markdown.markdown(
                p.body,
                extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc',
                    'markdown.extensions.fenced_code',
                ]
            )
        serializer = PostSerializer(posts, many=True)
        response = JsonResponse(serializer.data, safe=False)
        response['Access-Control-Allow-Origin'] = "*"
        return response


@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        cate_list = Category.objects.all()
        serializer = CateSerializer(cate_list, many=True)
        response = JsonResponse(serializer.data, safe=False)
        response['Access-Control-Allow-Origin'] = "*"
        return response


@csrf_exempt
def tag_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        response = JsonResponse(serializer.data, safe=False)
        response['Access-Control-Allow-Origin'] = "*"
        return response


@csrf_exempt
def achive_list(request):
    if request.method == 'GET':
        posts = Post.objects.dates('created_time', 'month', order='DESC')
        response = HttpResponse(posts)
        response['Access-Control-Allow-Origin'] = "*"
        return response
