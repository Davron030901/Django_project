# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Post
from rest_framework import permissions
from .serializers import PostSerializer,UserSerializer
from .permissions import IsOwnerOrReadOnly
# class PostListAPIView(ListCreateAPIView):
#     permission_classes = (IsOwnerOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
# class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsOwnerOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class UserListAPIView(ListCreateAPIView):
#     queryset =get_user_model().objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = (IsOwnerOrReadOnly,)
#
# class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer