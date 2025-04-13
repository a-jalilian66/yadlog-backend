from django.conf import settings
from django.utils.text import slugify


class TranslatedSlugMixin:
    slug_source_field = 'title'
    slug_field = 'slug'

    def generate_translated_slugs(self):
        for lang_code, _ in settings.LANGUAGES:
            slug_attr = f"{self.slug_field}_{lang_code}"
            title_attr = f"{self.slug_source_field}_{lang_code}"

            if not getattr(self, slug_attr, None) and getattr(self, title_attr, None):
                setattr(self, slug_attr, slugify(getattr(self, title_attr), allow_unicode=True))

    def save(self, *args, **kwargs):
        self.generate_translated_slugs()
        super().save(*args, **kwargs)
