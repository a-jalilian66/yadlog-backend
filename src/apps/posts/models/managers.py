from django.utils import timezone
from django.db import models
from .base import PostStatus
from django.utils.translation import get_language


class PublishedPostManager(models.Manager):
    def get_queryset(self):
        now = timezone.now()
        qs = super().get_queryset().filter(
            status=PostStatus.PUBLISHED,
        ).filter(
            models.Q(start_publication__lte=now) | models.Q(start_publication__isnull=True),
            models.Q(end_publication__gt=now) | models.Q(end_publication__isnull=True)
        )

        lang = get_language()
        slug_field = f"slug_{lang}"

        return qs.exclude(**{f"{slug_field}__isnull": True}).exclude(**{f"{slug_field}": ""})


class CategoryManager(models.Manager):
    def with_published_posts(self):
        now = timezone.now()
        lang = get_language()
        slug_field = f"slug_{lang}"
        post_slug_field = f"posts__slug_{lang}"

        qs = self.exclude(**{f"{slug_field}__isnull": True}).filter(
            posts__status=PostStatus.PUBLISHED,
            posts__start_publication__lt=now
        ).filter(
            models.Q(posts__end_publication__gt=now) | models.Q(posts__end_publication__isnull=True),
            ~models.Q(**{f"{post_slug_field}": ""}),
        ).distinct()
        return qs
