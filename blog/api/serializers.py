from blog.models import Post
from  rest_framework import serializers


class Postserializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["slug", "title", "body"]


class PostListserializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["user", "id", "slug", "title", "body", "created"]
