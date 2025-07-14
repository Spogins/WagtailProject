# -*- coding: utf-8 -*-
"""Core translations."""
from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from src.core.models import FormPage


#python manage.py fixtree
@register(FormPage)
class FormPageTranslationOptions(TranslationOptions):
    """Function index page translations."""
    fields = ("intro",)