from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BasePostModel
from .managers import PublishedPostManager
from apps.common.mixins.translated_slug import TranslatedSlugMixin
from ckeditor_uploader.fields import RichTextUploadingField

from ..utils import extract_toc_and_ids


class Post(TranslatedSlugMixin, BasePostModel):
    summary = RichTextUploadingField(_('Summary'), blank=True, null=True, config_name='awesome_ckeditor')
    content = RichTextUploadingField(_('Content'), config_name='awesome_ckeditor')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name=_('Category'))
    tags = models.ManyToManyField('Tag', blank=True, verbose_name=_('Tags'))
    toc = models.JSONField(_('Table of content'), blank=True, null=True)

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

    def save(self, *args, **kwargs):
        if self.content:
            updated_html, toc_list = extract_toc_and_ids(self.content)
            self.content = updated_html
            self.toc = toc_list
        super().save(*args, **kwargs)
