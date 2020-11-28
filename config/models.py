from django.db import models


class Entity(models.Model):
    class Meta:
        abstract = True


class AuditedEntity(Entity):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class FullAuditedEntity(AuditedEntity):
    is_deleted = models.BooleanField(
        default=False
    )
    deleted_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True