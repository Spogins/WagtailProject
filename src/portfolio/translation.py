from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from src.portfolio.models import PortfolioPage


#python manage.py fixtree
@register(PortfolioPage)
class PortfolioPageTranslationOptions(TranslationOptions):
    """Function index page translations."""
    fields = ("body",)