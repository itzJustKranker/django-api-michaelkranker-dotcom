from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post, Category, PostType
from rest_framework import serializers, viewsets, filters


class DefaultSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()


class PostTypeSerializer(DefaultSerializers):
    class Meta:
        model = PostType
        fields = '__all__'


class CategorySerializer(DefaultSerializers):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(DefaultSerializers):
    categories = CategorySerializer(many=True)
    type = PostTypeSerializer(many=False)

    class Meta:
        model = Post
        fields = '__all__'


default_search_fields = ['name', 'description']
default_ordering_fields = ['name', 'created_at', 'updated_at']


# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'type__name', 'categories__name']
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

