from modeltranslation.translator import register, TranslationOptions
from .models import Post, Category, Tag


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'content', 'slug')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'slug')


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('title', 'slug')
