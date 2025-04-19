from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _

from apps.common.mixins.translated_slug import TranslatedSlugMixin
from apps.posts.models.managers import CategoryManager


class Category(TranslatedSlugMixin, MPTTModel):
    title = models.CharField(_('Title'), max_length=100)
    slug = models.SlugField(
        _('Slug'),
        blank=True,
        unique=True,
        allow_unicode=True,
        help_text=_("Used to build category URL.")
    )
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children',
                            verbose_name=_('Parent'))

    objects = CategoryManager()

    def __str__(self):
        return f'{self.title}'

    _slug_separator = '/'
    _full_name_separator = ' > '

    @property
    def full_title(self):
        titles = [category.title for category in self.get_ancestors_and_self()]
        return self._full_name_separator.join(titles)

    def get_ancestors_and_self(self):
        if self.is_root():
            return [self]

        return list(self.get_ancestors()) + [self]

    class MPTTMeta:
        """
        Category MPTT meta information
        """
        order_insertion_by = ['title']

    class Meta:
        """
        Categories meta information
        """
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
