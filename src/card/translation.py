from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from src.card.models import CardIndexPage, CardPage


@register(CardIndexPage)
class CardIndexPageTranslationOptions(TranslationOptions):
    fields = ("intro",)

@register(CardPage)
class CardPageTranslationOptions(TranslationOptions):
    fields = ("intro", "body",)

