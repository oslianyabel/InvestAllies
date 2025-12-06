from __future__ import annotations

import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.text import slugify

try:
    from faker import Faker
except Exception:  # pragma: no cover - instruct user to install
    Faker = None  # type: ignore

from app.models import (
    Article,
    ArticleCategory,
    Country,
    FuelPrice,
    InvestmentObject,
    LandingPage,
    Lead,
    MetalPrice,
    Service,
    SocialLink,
    SocialPlatform,
)


class Command(BaseCommand):
    help = "Seed database with fake data for development"

    def add_arguments(self, parser) -> None:
        parser.add_argument("--countries", type=int, default=5)
        parser.add_argument("--services", type=int, default=5)
        parser.add_argument("--articles", type=int, default=20)
        parser.add_argument("--objects", type=int, default=12)
        parser.add_argument("--socials", type=int, default=6)

    def handle(self, *args, **options) -> None:
        if Faker is None:
            self.stderr.write("Faker is not installed. Install with: pip install Faker")
            return

        fake = Faker()
        now = timezone.now()

        # Countries
        countries = []
        for _ in range(options["countries"]):
            name = fake.country()
            slug = slugify(name)[:50]
            obj, created = Country.objects.get_or_create(
                slug=slug, defaults={"name": name, "active": True}
            )
            countries.append(obj)

        # Services
        services = []
        for _ in range(options["services"]):
            title = fake.sentence(nb_words=3).rstrip(".")
            slug = slugify(title)[:50]
            svc, _ = Service.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": title,
                    "description": fake.paragraph(),
                    "active": True,
                },
            )
            services.append(svc)

        # Article categories (ensure some known categories exist)
        known = ["gold", "fuel", "legal", "offshore", "investments"]
        categories = []
        for name in known:
            cat, _ = ArticleCategory.objects.get_or_create(
                slug=name, defaults={"name": name.title()}
            )
            categories.append(cat)

        # Additional random categories
        for _ in range(3):
            title = fake.word()
            slug = slugify(title)[:50]
            cat, _ = ArticleCategory.objects.get_or_create(
                slug=slug, defaults={"name": title.title()}
            )
            categories.append(cat)

        # Articles
        for _ in range(options["articles"]):
            title = fake.sentence(nb_words=6)
            # Article model does not have a `slug` field; use title as unique lookup
            cat = random.choice(categories)
            country = (
                random.choice(countries)
                if countries and random.random() < 0.6
                else None
            )
            Article.objects.get_or_create(
                title=title,
                defaults={
                    "content": fake.paragraph(nb_sentences=5),
                    "category": cat,
                    "country": country,
                    "publish": True,
                },
            )

        # Investment objects
        for _ in range(options["objects"]):
            title = fake.sentence(nb_words=4).rstrip(".")
            slug = slugify(title)[:50]
            country = random.choice(countries) if countries else None
            price = Decimal(random.randint(5_000, 2_000_000))
            roi = Decimal(random.uniform(3.0, 25.0)).quantize(Decimal("0.01"))
            InvestmentObject.objects.get_or_create(
                title=title,
                defaults={
                    "description": fake.paragraph(nb_sentences=3),
                    "country": country,
                    "price": price,
                    "expected_roi": roi,
                    "active": True,
                    "images": [fake.image_url() for _ in range(2)],
                },
            )

        # Landing pages
        for svc in services:
            slug = f"landing-{svc.slug}"
            LandingPage.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": f"{svc.title} - Landing",
                    "content": fake.paragraph(nb_sentences=6),
                    "service": svc,
                    "publish": True,
                },
            )

        # Leads (sample)
        for _ in range(6):
            Lead.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                message=fake.sentence(nb_words=10),
                source=random.choice(["form", "landing", "article"]),
            )

        # Metal prices
        MetalPrice.objects.create(metal="gold", price=Decimal("1950.25"), timestamp=now)
        MetalPrice.objects.create(metal="silver", price=Decimal("23.12"), timestamp=now)

        # Fuel price
        FuelPrice.objects.create(
            fuel_type="Fuel Platts",
            price=Decimal("78.45"),
            currency="USD",
            timestamp=now,
        )

        # Social links (create entries for each platform up to requested number)
        platforms = [p.value for p in SocialPlatform]
        created_links = 0
        for p in platforms:
            if created_links >= options["socials"]:
                break
            url = f"https://{p}.example.com/{slugify(fake.word())}"
            SocialLink.objects.get_or_create(
                platform=p,
                defaults={"url": url, "active": True, "order": created_links},
            )
            created_links += 1

        self.stdout.write(self.style.SUCCESS("Seeding completed."))
