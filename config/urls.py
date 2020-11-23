from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from posts.urls import PostViewSet, PostTypeViewSet, CategoryViewSet


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.StringRelatedField(many=True, read_only=True)
    user_permissions = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        exclude = ['password']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'post-types', PostTypeViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
