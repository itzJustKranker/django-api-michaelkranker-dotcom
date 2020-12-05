from django.db import models
from config.models import AuditedEntity, FullAuditedEntity


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

