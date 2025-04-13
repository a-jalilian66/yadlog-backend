from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    slug = models.SlugField(_('Slug'), unique=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return f'{self.title}'
