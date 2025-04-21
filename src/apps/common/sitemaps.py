from django.contrib.sitemaps import Sitemap
from django.conf import settings
from django.urls import reverse
from django.utils import translation
from apps.posts.models import Post, Tag, Category


class PostSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    i18n = True
    x_default = True
    protocol = 'https'

    def items(self):
        # Only published and viewable posts
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated_at

    def get_languages_for_item(self, item):
        if not self.i18n:
            return [settings.LANGUAGE_CODE]

        # Only languages that actually have translations
        langs = []
        for lang_code, _ in settings.LANGUAGES:
            slug_field = f"slug_{lang_code}"
            if getattr(item, slug_field, None):
                langs.append(lang_code)
        return langs


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.5
    i18n = True
    x_default = True
    protocol = 'https'

    def items(self):
        return ['posts:home']  # Only pages that are multilingual

    def location(self, name):
        with translation.override(settings.LANGUAGE_CODE):
            return reverse(name)

    def get_languages_for_item(self, item):
        if not self.i18n:
            return [settings.LANGUAGE_CODE]
        return [lang_code for lang_code, _ in settings.LANGUAGES]


class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7
    i18n = True
    x_default = True
    protocol = 'https'

    def items(self):
        return Category.objects.with_published_posts()

    def location(self, obj):
        with translation.override(settings.LANGUAGE_CODE):
            return reverse('posts:category_detail', kwargs={'slug': obj.slug})

    def lastmod(self, obj):
        latest = obj.posts.filter(status='published').order_by('-updated_at').first()
        return latest.updated_at if latest else None

    def get_languages_for_item(self, item):
        if not self.i18n:
            return [settings.LANGUAGE_CODE]

        # Only languages that actually have translations
        langs = []
        for lang_code, _ in settings.LANGUAGES:
            slug_field = f"slug_{lang_code}"
            if getattr(item, slug_field, None):
                langs.append(lang_code)
        return langs


class TagSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6
    i18n = True
    x_default = True
    protocol = 'https'

    def items(self):
        return Tag.objects.filter(posts__status='published').distinct()

    def lastmod(self, obj):
        latest = obj.posts.filter(status='published').order_by('-updated_at').first()
        return latest.updated_at if latest else None

    def get_languages_for_item(self, item):
        if not self.i18n:
            return [settings.LANGUAGE_CODE]

        # Only languages that actually have translations
        langs = []
        for lang_code, _ in settings.LANGUAGES:
            slug_field = f"slug_{lang_code}"
            if getattr(item, slug_field, None):
                langs.append(lang_code)
        return langs
