from django.contrib import admin
from .models import Contact, RequestForProposal


default_fields = ('name', 'email', 'created_at', 'updated_at')


class BaseAdminModel(admin.ModelAdmin):
    list_display = default_fields


admin.site.register(Contact, BaseAdminModel)
admin.site.register(RequestForProposal, BaseAdminModel)
