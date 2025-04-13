from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', 'slug', 'publication_date',)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('title', 'parent')


@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    list_display = ('title',)
