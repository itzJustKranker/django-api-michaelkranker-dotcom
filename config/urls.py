from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from config import settings
from contact.urls import ContactViewSet, RFPViewSet
from posts.urls import PostViewSet, PostTypeViewSet, CategoryViewSet


class UserSerializer(serializers.ModelSerializer):
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
router.register(r'contacts', ContactViewSet)
router.register(r'rfps', RFPViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
