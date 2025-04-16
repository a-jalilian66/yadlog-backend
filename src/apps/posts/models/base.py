from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.utils.text import slugify as django_slugify


class PostStatus(models.TextChoices):
    DRAFT = 'draft', _('Draft')
    HIDDEN = 'hidden', _('Hidden')
    PUBLISHED = 'published', _('published')


class BasePostModel(models.Model):
    title = models.CharField(_('Title'), max_length=255)

    slug = models.SlugField(
        blank=True,
        unique=True,
        allow_unicode=True,
        help_text=_("Used in the URL of the post.")
    )

    status = models.CharField(_('Status'), choices=PostStatus.choices, max_length=10, default=PostStatus.DRAFT)
    publication_date = models.DateTimeField(_('Publication Date'), null=True, blank=True)

    start_publication = models.DateTimeField(_('Start publication'), blank=True, null=True)
    end_publication = models.DateTimeField(_('End publication'), blank=True, null=True)

    created_at = models.DateTimeField(_('Created on'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Last Updated'), auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-publication_date']
        get_latest_by = 'publication_date'

    @property
    def is_actual(self):
        now = timezone.now()
        if self.start_publication and now < self.start_publication:
            return False
        if self.end_publication and now >= self.end_publication:
            return False
        return True

    @property
    def is_visible(self):
        return self.status == PostStatus.PUBLISHED and self.is_actual

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title} ({self.status})'
