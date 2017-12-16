from blog.models import Post
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, \
    UpdateAPIView
from .serializers import Postserializers, PostListserializers
from .permissions import IsownerorReadonly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q
from rest_framework.filters import OrderingFilter, SearchFilter
from .pagination import PostLimitoffsetPagination, PostNumberpagePagination


class PostCreateApi(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostUpdateApi(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializers
    permission_classes = [IsAuthenticatedOrReadOnly, IsownerorReadonly]

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
    serializer_class = PostListserializers
    filter_backends = [SearchFilter]
    search_fields = ["title", "body", "user__username"]
    pagination_class = PostNumberpagePagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(slug__icontains=query) |
                Q(user__username__icontains=query)
            ).distinct()

        return queryset_list
