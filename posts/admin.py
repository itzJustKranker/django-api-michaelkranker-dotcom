from django.contrib import admin
from .models import Category, PostType, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(PostType, PostTypeAdmin)
admin.site.register(Post, PostAdmin)
