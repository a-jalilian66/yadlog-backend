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
