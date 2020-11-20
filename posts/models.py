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
    is_deleted = models.BinaryField(
        default=False
    )
    deleted_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class Category(AuditedEntity):
    name = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=250
    )


class PostType(AuditedEntity):
    name = models.CharField(
        max_length=100
    )


class Post(FullAuditedEntity):
    DRAFT = 0
    PENDING = 1
    PUBLISHED = 2
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PENDING, 'Pending'),
        (PUBLISHED, 'Published'),
    )
    title = models.CharField(
        max_length=250
    )
    body = models.TextField()
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0
    )
    featured_image = models.FilePathField("/featured_images")
    categories = models.ManyToManyField(
        Category,
        related_name='post_category'
    )
    type = models.OneToOneField(
        PostType,
        related_name='post_type',
        on_delete=models.CASCADE
    )

