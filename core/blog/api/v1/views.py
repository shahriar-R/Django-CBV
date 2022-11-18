
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import CategorySerializer, PostSerializer
from ...models import Category, Post
from .paginations import CustomPagination


'''
from rest_framework.decorators import api_view, permission_classes

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
'''

'''class PostList(APIView):
    """geting a list of posts and creating new post"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self,request):
        """retriving a list of posts"""
        posts = Post.objects.filter(status=True)
        serializer - PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request):
        """creating a post with provided data"""
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''

class PostList(ListCreateAPIView):
    """geting a list of posts and creating new post"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)



'''class PostDetail(APIView):
    """getting detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self,request,id):
        """retriving the post data"""
        post = get_object_or_404(pk=id,status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data) 

    def put(self,request,id):
        """editing the post data"""
        post = get_object_or_404(pk=id,status=True)
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,id):
        post = get_object_or_404(pk=id,status=True)
        post.delete()
        return Response({"delete":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)'''

'''class PostDetail(GenericAPIView,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self,request, *args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request, *args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request, *args,**kwargs):
        return self.destroy(request,*args,**kwargs)'''

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


    
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = {'category':["exact","in"],'author':["exact"],'status':["exact"]}
    search_fields = ['title','context']
    ordering_fields = ['create_date']
    pagination_class = CustomPagination

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

 
 
    