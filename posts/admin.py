from django.contrib import admin
from .models import Category, PostType, Post


default_fields = ('name', 'created_at', 'updated_at')


class BaseAdminModel(admin.ModelAdmin):
    list_display = default_fields


admin.site.register(Category, BaseAdminModel)
admin.site.register(PostType, BaseAdminModel)
admin.site.register(Post, BaseAdminModel)
