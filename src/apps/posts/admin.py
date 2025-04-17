from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Post, Category, Tag
from ..common.mixins.translation_mptt_admin import TranslationDraggableMPTTAdmin


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', 'slug', 'publication_date',)


@admin.register(Category)
class CategoryAdmin(TranslationDraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)


@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    list_display = ('title',)
