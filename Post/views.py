from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Post.models import Post, Category, Tag
from Post.serializers import PostSerializer, CateSerializer, TagSerializer


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
        tag_list = Tag.objects.all()
        serializer = TagSerializer(tag_list, many=True)
        response = JsonResponse(serializer.data, safe=False)
        response['Access-Control-Allow-Origin'] = "*"
        return response
