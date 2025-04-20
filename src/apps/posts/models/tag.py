from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.mixins.translated_slug import TranslatedSlugMixin


class Tag(TranslatedSlugMixin, models.Model):
    title = models.CharField(_('Title'), max_length=50)
    slug = models.SlugField(
        blank=True,
        unique=True,
        allow_unicode=True,
        help_text=_("Used to build category URL.")
    )

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return f'{self.title}'
