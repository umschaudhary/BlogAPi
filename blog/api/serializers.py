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
    user = serializers.SerializerMethodField()
    # image = serializers.SerializerMethodField

    delete_url = serializers.HyperlinkedIdentityField(
        view_name="api:delete",
    )

    class Meta:
        model = Post
        fields = ["user", "url", "slug", "title", "body", "created", "delete_url"]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None

        return image
