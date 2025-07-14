# -*- coding: utf-8 -*-
from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from src.blog.models import BlogIndexPage, BlogPage, BlogPageGalleryImage, Author, BlogTagIndexPage


@register(BlogIndexPage)
class BlogIndexPageTranslationOptions(TranslationOptions):
    """Function index page translations."""
    fields = ("intro",)


@register(BlogPage)
class BlogPageTranslationOptions(TranslationOptions):
    """Function index page translations."""
    fields = ("date", "intro", "body",)


@register(BlogPageGalleryImage)
class BlogPageGalleryImageTranslationOptions(TranslationOptions):
    """Function index page translations."""
    fields = ("image", "caption",)


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    """Function index page translations."""
    fields = ("name", "author_image",)

@register(BlogTagIndexPage)
class BlogTagIndexPageTranslationOptions(TranslationOptions):
    """Function index page translations."""
    fields = ("intro",)

