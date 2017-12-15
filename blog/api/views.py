from blog.models import Post
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, \
    UpdateAPIView
from .serializers import Postserializers, PostListserializers


class PostCreateApi(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostUpdateApi(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializers

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostDestroyApi(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListserializers


class PostDetailApi(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListserializers


class PostDetailsApi(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListserializers
    lookup_field = 'slug'


class PostListApi(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListserializers
