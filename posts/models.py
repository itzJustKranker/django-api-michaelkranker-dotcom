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


class Category(AuditedEntity):
    name = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=250
    )

    def __str__(self):
        return self.name


class PostType(AuditedEntity):
    name = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=250
    )

    def __str__(self):
        return self.name


class Post(FullAuditedEntity):
    class Status(models.IntegerChoices):
        DRAFT = 0
        PENDING = 1
        PUBLISHED = 2
    name = models.CharField(
        max_length=250
    )
    description = models.TextField()
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.DRAFT
    )
    featured_image = models.ImageField(upload_to="photos/%Y/%m/%d")
    categories = models.ManyToManyField(
        Category
    )
    type = models.ForeignKey(
        PostType,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

