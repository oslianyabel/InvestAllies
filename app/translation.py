from modeltranslation.translator import TranslationOptions, register

from .models import (
    Article,
    ArticleCategory,
    Country,
    InvestmentObject,
    LandingPage,
    Service,
)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ("name", "slug")


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ("title", "description", "slug")


@register(ArticleCategory)
class ArticleCategoryTranslationOptions(TranslationOptions):
    fields = ("name", "slug")


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ("title", "content", "slug")


@register(InvestmentObject)
class InvestmentObjectTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(LandingPage)
class LandingPageTranslationOptions(TranslationOptions):
    fields = ("title", "content", "slug")
