import logging
from typing import Any, Dict

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import (
    Article,
    Country,
    FuelPrice,
    InvestmentObject,
    LandingPage,
    MetalPrice,
    Service,
)

# Logger for views
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    handler.setFormatter(fmt)
    logger.addHandler(handler)


def home(request: HttpRequest) -> HttpResponse:
    logger.info("home called")
    countries = Country.objects.filter(active=True)
    featured_objects = InvestmentObject.objects.filter(active=True)[:6]
    latest_articles = Article.objects.filter(publish=True).order_by("-created_at")[:5]
    ctx: Dict[str, Any] = {
        "countries": countries,
        "featured_objects": featured_objects,
        "latest_articles": latest_articles,
    }
    return render(request, "app/home.html", ctx)


def investments_index(request: HttpRequest) -> HttpResponse:
    logger.info("investments_index called")
    countries = Country.objects.filter(active=True)
    return render(request, "app/investments_index.html", {"countries": countries})


def country_detail(request: HttpRequest, country_slug: str) -> HttpResponse:
    logger.info(f"country_detail called country_slug={country_slug}")
    country = get_object_or_404(Country, slug=country_slug, active=True)
    articles = Article.objects.filter(country=country, publish=True).order_by(
        "-created_at"
    )
    objects = InvestmentObject.objects.filter(country=country, active=True)
    return render(
        request,
        "app/country_detail.html",
        {"country": country, "articles": articles, "objects": objects},
    )


def country_articles(request: HttpRequest, country_slug: str) -> HttpResponse:
    logger.info(f"country_articles called country_slug={country_slug}")
    country = get_object_or_404(Country, slug=country_slug, active=True)
    articles = Article.objects.filter(country=country, publish=True).order_by(
        "-created_at"
    )
    return render(
        request,
        "app/country_articles.html",
        {"country": country, "articles": articles},
    )


def article_detail(request: HttpRequest, pk: int) -> HttpResponse:
    logger.info(f"article_detail called pk={pk}")
    article = get_object_or_404(Article, pk=pk, publish=True)
    return render(request, "app/article_detail.html", {"article": article})


def country_objects(request: HttpRequest, country_slug: str) -> HttpResponse:
    logger.info(f"country_objects called country_slug={country_slug}")
    country = get_object_or_404(Country, slug=country_slug, active=True)
    objects = InvestmentObject.objects.filter(country=country, active=True)
    return render(
        request,
        "app/country_objects.html",
        {"country": country, "objects": objects},
    )


def object_detail(request: HttpRequest, pk: int) -> HttpResponse:
    logger.info(f"object_detail called pk={pk}")
    obj = get_object_or_404(InvestmentObject, pk=pk, active=True)
    return render(request, "app/object_detail.html", {"object": obj})


def gold_index(request: HttpRequest) -> HttpResponse:
    logger.info("gold_index called")
    latest = MetalPrice.objects.filter(metal="gold").first()
    articles = Article.objects.filter(category__slug="gold")[:10]
    return render(
        request, "app/gold_index.html", {"price": latest, "articles": articles}
    )


def gold_price(request: HttpRequest) -> HttpResponse:
    logger.info("gold_price called")
    latest = MetalPrice.objects.filter(metal="gold").first()
    return render(request, "app/gold_price.html", {"price": latest})


def gold_calculator(request: HttpRequest) -> HttpResponse:
    logger.info("gold_calculator called")
    return render(request, "app/gold_calculator.html", {})


def gold_articles(request: HttpRequest) -> HttpResponse:
    logger.info("gold_articles called")
    articles = Article.objects.filter(category__slug="gold", publish=True)
    return render(request, "app/gold_articles.html", {"articles": articles})


def gold_buy(request: HttpRequest) -> HttpResponse:
    logger.info("gold_buy called")
    products = []
    return render(request, "app/gold_buy.html", {"products": products})


def fuel_index(request: HttpRequest) -> HttpResponse:
    logger.info("fuel_index called")
    latest = FuelPrice.objects.first()
    return render(request, "app/fuel_index.html", {"price": latest})


def fuel_price(request: HttpRequest) -> HttpResponse:
    logger.info("fuel_price called")
    latest = FuelPrice.objects.first()
    return render(request, "app/fuel_price.html", {"price": latest})


def fuel_calculator(request: HttpRequest) -> HttpResponse:
    logger.info("fuel_calculator called")
    return render(request, "app/fuel_calculator.html", {})


def fuel_articles(request: HttpRequest) -> HttpResponse:
    logger.info("fuel_articles called")
    articles = Article.objects.filter(category__slug="fuel", publish=True)
    return render(request, "app/fuel_articles.html", {"articles": articles})


def fuel_offers(request: HttpRequest) -> HttpResponse:
    logger.info("fuel_offers called")
    offers = []
    return render(request, "app/fuel_offers.html", {"offers": offers})


def offshore_index(request: HttpRequest) -> HttpResponse:
    logger.info("offshore_index called")
    return render(request, "app/offshore_index.html", {})


def offshore_jurisdictions(request: HttpRequest) -> HttpResponse:
    logger.info("offshore_jurisdictions called")
    return render(request, "app/offshore_jurisdictions.html", {})


def offshore_services(request: HttpRequest) -> HttpResponse:
    logger.info("offshore_services called")
    services = Service.objects.filter(active=True)
    return render(request, "app/offshore_services.html", {"services": services})


def legal_index(request: HttpRequest) -> HttpResponse:
    logger.info("legal_index called")
    return render(request, "app/legal_index.html", {})


def legal_articles(request: HttpRequest) -> HttpResponse:
    logger.info("legal_articles called")
    articles = Article.objects.filter(category__slug="legal", publish=True)
    return render(request, "app/legal_articles.html", {"articles": articles})


def services_index(request: HttpRequest) -> HttpResponse:
    logger.info("services_index called")
    services = Service.objects.filter(active=True)
    return render(request, "app/services_index.html", {"services": services})


def service_detail(request: HttpRequest, slug: str) -> HttpResponse:
    logger.info(f"service_detail called slug={slug}")
    service = get_object_or_404(Service, slug=slug, active=True)
    return render(request, "app/service_detail.html", {"service": service})


def landing_page(request: HttpRequest, slug: str) -> HttpResponse:
    logger.info(f"landing_page called slug={slug}")
    landing = get_object_or_404(LandingPage, slug=slug, publish=True)
    return render(request, "app/landing_page.html", {"landing": landing})


def search(request: HttpRequest) -> HttpResponse:
    q = request.GET.get("q", "").strip()
    logger.info(f"search called q={q}")
    articles = Article.objects.filter(title__icontains=q)[:20] if q else []
    objects = InvestmentObject.objects.filter(title__icontains=q)[:20] if q else []
    return render(
        request, "app/search.html", {"q": q, "articles": articles, "objects": objects}
    )


def subscribe(request: HttpRequest) -> HttpResponse:
    logger.info(f"subscribe called method={request.method}")
    if request.method == "POST":
        # minimal handling: create Lead entry or similar in future
        return render(request, "app/subscribe_thanks.html", {})
    return render(request, "app/subscribe.html", {})


def api_gold_price(request: HttpRequest) -> JsonResponse:
    logger.info("api_gold_price called")
    latest = MetalPrice.objects.filter(metal="gold").first()
    data: Dict[str, Any] = {
        "metal": "gold",
        "price": str(latest.price) if latest else None,
        "timestamp": latest.timestamp.isoformat() if latest else None,
        "currency": "USD",
    }
    return JsonResponse(data)


def api_fuel_price(request: HttpRequest) -> JsonResponse:
    logger.info("api_fuel_price called")
    latest = FuelPrice.objects.first()
    data: Dict[str, Any] = {
        "fuel": latest.fuel_type if latest else "platts",
        "price": str(latest.price) if latest else None,
        "timestamp": latest.timestamp.isoformat() if latest else None,
        "currency": latest.currency if latest else "USD",
    }
    return JsonResponse(data)
