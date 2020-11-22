from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post, Category, PostType
from rest_framework import serializers, viewsets, filters


default_search_fields = ['name', 'description']
default_ordering_fields = ['name', 'created_at', 'updated_at']


# Serializers define the API representation.
class PostSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.StringRelatedField(many=True, read_only=True)
    type = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostType
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'status', 'categories']
    ordering_fields = default_ordering_fields
    search_fields = default_search_fields


class PostTypeViewSet(viewsets.ModelViewSet):
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = default_search_fields


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = default_search_fields

