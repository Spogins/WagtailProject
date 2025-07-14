# -*- coding: utf-8 -*-
"""Home translations."""
from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from src.home.models import HomePage

#python manage.py fixtree
@register(HomePage)
class HomePageTranslationOptions(TranslationOptions):
    """Function index page translations."""
    fields = ("body",)