from django.contrib import admin

from .models import (
    Article,
    ArticleCategory,
    Country,
    FuelPrice,
    InvestmentObject,
    LandingPage,
    Lead,
    LiveDataCache,
    MetalPrice,
    Service,
)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "active")
    search_fields = ("name", "slug")
    list_filter = ("active",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "active")
    search_fields = ("title", "slug")
    list_filter = ("active",)


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "country", "publish", "created_at")
    search_fields = ("title", "content")
    list_filter = ("publish", "category", "country")
    date_hierarchy = "created_at"


@admin.register(InvestmentObject)
class InvestmentObjectAdmin(admin.ModelAdmin):
    list_display = ("title", "country", "price", "expected_roi", "active")
    search_fields = ("title", "description")
    list_filter = ("country", "active")


@admin.register(LandingPage)
class LandingPageAdmin(admin.ModelAdmin):
    list_display = ("slug", "title", "service", "publish")
    search_fields = ("slug", "title")
    list_filter = ("publish",)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "source", "created_at")
    search_fields = ("name", "email", "phone", "message")
    list_filter = ("source",)
    readonly_fields = ("created_at",)


@admin.register(LiveDataCache)
class LiveDataCacheAdmin(admin.ModelAdmin):
    list_display = ("key", "timestamp")
    search_fields = ("key",)


@admin.register(MetalPrice)
class MetalPriceAdmin(admin.ModelAdmin):
    list_display = ("metal", "price", "timestamp")
    list_filter = ("metal",)
    date_hierarchy = "timestamp"


@admin.register(FuelPrice)
class FuelPriceAdmin(admin.ModelAdmin):
    list_display = ("fuel_type", "price", "currency", "timestamp")
    list_filter = ("fuel_type", "currency")
    date_hierarchy = "timestamp"
