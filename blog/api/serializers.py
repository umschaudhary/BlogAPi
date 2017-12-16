from blog.models import Post
from  rest_framework import serializers


class Postserializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["slug", "title", "body"]


class PostListserializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:detail",
    )

    delete_url = serializers.HyperlinkedIdentityField(
        view_name="api:delete",
    )

    class Meta:
        model = Post
        fields = ["user", "url", "slug", "title", "body", "created", "delete_url"]
