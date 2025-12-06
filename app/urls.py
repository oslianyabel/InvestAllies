from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.home, name="home"),
    # Investments by country
    path("investments/", views.investments_index, name="investments_index"),
    path(
        "investments/<slug:country_slug>/", views.country_detail, name="country_detail"
    ),
    path(
        "investments/<slug:country_slug>/articles/",
        views.country_articles,
        name="country_articles",
    ),
    path("articles/<slug:slug>/", views.article_detail, name="article_detail"),
    path(
        "investments/<slug:country_slug>/objects/",
        views.country_objects,
        name="country_objects",
    ),
    path("objects/<slug:slug>/", views.object_detail, name="object_detail"),
    # Gold
    path("gold/", views.gold_index, name="gold_index"),
    path("gold/price/", views.gold_price, name="gold_price"),
    path("gold/calculator/", views.gold_calculator, name="gold_calculator"),
    path("gold/articles/", views.gold_articles, name="gold_articles"),
    path("gold/buy/", views.gold_buy, name="gold_buy"),
    # Fuel
    path("fuel/", views.fuel_index, name="fuel_index"),
    path("fuel/price/", views.fuel_price, name="fuel_price"),
    path("fuel/calculator/", views.fuel_calculator, name="fuel_calculator"),
    path("fuel/articles/", views.fuel_articles, name="fuel_articles"),
    path("fuel/offers/", views.fuel_offers, name="fuel_offers"),
    # Offshore
    path("offshore/", views.offshore_index, name="offshore_index"),
    path(
        "offshore/jurisdictions/",
        views.offshore_jurisdictions,
        name="offshore_jurisdictions",
    ),
    path("offshore/services/", views.offshore_services, name="offshore_services"),
    # Legal & Banking
    path("legal/", views.legal_index, name="legal_index"),
    path("legal/articles/", views.legal_articles, name="legal_articles"),
    # Services and consultancy
    path("services/", views.services_index, name="services_index"),
    path("services/<slug:slug>/", views.service_detail, name="service_detail"),
    # Landing pages
    path("landing/<slug:slug>/", views.landing_page, name="landing_page"),
    # Utilities
    path("search/", views.search, name="search"),
    path("subscribe/", views.subscribe, name="subscribe"),
]
