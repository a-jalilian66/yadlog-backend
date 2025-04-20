from django.utils.text import slugify
from modeltranslation.utils import build_localized_fieldname
from modeltranslation.settings import AVAILABLE_LANGUAGES


class TranslatedSlugMixin:
    slug_source_field = 'title'
    slug_field = 'slug'

    def generate_translated_slugs(self):
        """
        For each active modeltranslation language
        If the title field is filled but the slug is empty,
        create a new slug.
        """
        for lang in AVAILABLE_LANGUAGES:
            slug_attr = build_localized_fieldname(self.slug_field, lang)
            title_attr = build_localized_fieldname(self.slug_source_field, lang)
            title_val = getattr(self, title_attr, None)
            if title_val and not getattr(self, slug_attr, None):
                setattr(
                    self,
                    slug_attr,
                    slugify(title_val, allow_unicode=True)
                )

    def save(self, *args, **kwargs):
        self.generate_translated_slugs()
        super().save(*args, **kwargs)
