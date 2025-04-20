from django.utils import timezone
from django.db import models
from .base import PostStatus


class PublishedPostManager(models.Manager):
    def get_queryset(self):
        now = timezone.now()
        return super().get_queryset().filter(
            status=PostStatus.PUBLISHED,
        ).filter(
            models.Q(start_publication__lte=now) | models.Q(start_publication__isnull=True),
            models.Q(end_publication__gt=now) | models.Q(end_publication__isnull=True)
        )


class CategoryManager(models.Manager):
    def with_published_posts(self):
        now = timezone.now()
        return self.filter(
            posts__status=PostStatus.PUBLISHED,
            posts__start_publication__lt=now
        ).filter(
            models.Q(posts__end_publication__gt=now) | models.Q(posts__end_publication__isnull=True)).distinct()
