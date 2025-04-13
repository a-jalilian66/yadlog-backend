from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BasePostModel
from .managers import PublishedPostManager
from apps.common.mixins.translated_slug import TranslatedSlugMixin


class Post(TranslatedSlugMixin, BasePostModel):
    summary = models.TextField(_('Summary'), blank=True, null=True)
    content = models.TextField(_('Content'))
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name=_('Category'))
    tags = models.ManyToManyField('Tag', blank=True, verbose_name=_('Tags'))

    objects = models.Manager()
    published = PublishedPostManager()

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    indexes = [
        models.Index(fields=['slug']),
        models.Index(fields=['status']),
        models.Index(fields=['status', 'publication_date']),
        models.Index(fields=['publication_date']),
    ]

    models.UniqueConstraint(
        fields=['slug', 'publication_date'],
        name='unique_slug_per_day'
    )
