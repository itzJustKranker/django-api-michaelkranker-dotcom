from posts.models import Post
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class PostSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.StringRelatedField(many=True, read_only=True)
    type = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

