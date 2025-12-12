from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

try:
    # Ensure translation registration runs before admin classes are instantiated
    from . import translation  # noqa: F401
except ImportError:
    # If translations can't be imported in some environments, proceed and
    # let modeltranslation raise a clear error later when required.
    pass

from modeltranslation.admin import TranslationAdmin

from .models import (
    Article,
    ArticleCategory,
    Country,
    FuelPrice,
    InvestmentObject,
    LandingPage,
    Lead,
    MetalPrice,
    Service,
)

admin.site.site_header = "Invest Allies"
admin.site.site_title = "Invest Allies admin"
admin.site.index_title = "Welcome to the Invest Allies administration portal"


class CountryResource(resources.ModelResource):
    class Meta:
        model = Country


class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service


class ArticleCategoryResource(resources.ModelResource):
    class Meta:
        model = ArticleCategory


class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article


class InvestmentObjectResource(resources.ModelResource):
    class Meta:
        model = InvestmentObject


class LandingPageResource(resources.ModelResource):
    class Meta:
        model = LandingPage


class LeadResource(resources.ModelResource):
    class Meta:
        model = Lead


class MetalPriceResource(resources.ModelResource):
    class Meta:
        model = MetalPrice


class FuelPriceResource(resources.ModelResource):
    class Meta:
        model = FuelPrice


@admin.register(Country)
class CountryAdmin(TranslationAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CountryResource
    list_display = ("name", "slug", "active")
    search_fields = ("name", "slug")
    list_filter = ("active",)


@admin.register(Service)
class ServiceAdmin(TranslationAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ServiceResource
    list_display = ("title", "slug", "active")
    search_fields = ("title", "slug")
    list_filter = ("active",)


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(TranslationAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ArticleCategoryResource
    list_display = ("name", "slug")
    search_fields = ("name", "slug")


@admin.register(Article)
class ArticleAdmin(TranslationAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ArticleResource
    list_display = ("title", "category", "country", "publish", "created_at")
    search_fields = ("title", "content")
    list_filter = ("publish", "category", "country")
    date_hierarchy = "created_at"


@admin.register(InvestmentObject)
class InvestmentObjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = InvestmentObjectResource
    list_display = ("title", "country", "price", "expected_roi", "active")
    search_fields = ("title", "description")
    list_filter = ("country", "active")


@admin.register(LandingPage)
class LandingPageAdmin(TranslationAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LandingPageResource
    list_display = ("slug", "title", "service", "publish")
    search_fields = ("slug", "title")
    list_filter = ("publish",)


@admin.register(Lead)
class LeadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LeadResource
    list_display = ("name", "email", "phone", "source", "created_at")
    search_fields = ("name", "email", "phone", "message")
    list_filter = ("source",)
    readonly_fields = ("created_at",)


@admin.register(MetalPrice)
class MetalPriceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MetalPriceResource
    list_display = ("metal", "price", "timestamp")
    list_filter = ("metal",)
    date_hierarchy = "timestamp"


@admin.register(FuelPrice)
class FuelPriceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FuelPriceResource
    list_display = ("fuel_type", "price", "currency", "timestamp")
    list_filter = ("fuel_type", "currency")
    date_hierarchy = "timestamp"
