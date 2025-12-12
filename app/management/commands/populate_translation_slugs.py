from __future__ import annotations

from typing import Iterable

from django.core.management.base import BaseCommand
from django.db import transaction

from app.models import (
    Article,
    ArticleCategory,
    Country,
    LandingPage,
    Service,
)


def _iter_models() -> Iterable[type]:
    """Return list of models to populate translation slugs for."""
    return [Country, Service, ArticleCategory, Article, LandingPage]


class Command(BaseCommand):
    help = "Populate per-language slugs for translatable models by saving instances."

    def handle(self, *args, **options):
        for Model in _iter_models():
            qs = Model.objects.all()
            count = qs.count()
            if count == 0:
                self.stdout.write(
                    self.style.NOTICE(f"No {Model.__name__} items to process")
                )
                continue
            self.stdout.write(
                self.style.SUCCESS(f"Processing {count} {Model.__name__} objects...")
            )
            with transaction.atomic():
                for i, obj in enumerate(qs, start=1):
                    # Save will trigger SlugMixin logic to populate slugs per language
                    obj.save()
                    if i % 50 == 0:
                        self.stdout.write(f"  - processed {i}/{count}")
            self.stdout.write(
                self.style.SUCCESS(f"Finished {Model.__name__} ({count})")
            )
