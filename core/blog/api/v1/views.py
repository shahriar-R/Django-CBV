from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer
from ...models import Post


@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer - PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request,id):
    post = get_object_or_404(pk=id,status=True)
    if request.method == "GET":
        serializer - PostSerializer(post,many=True)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"delete":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)

 
    