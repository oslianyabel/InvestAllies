from enum import StrEnum
from typing import Any

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify


class SlugMixin:
    """Mixin to auto-generate a unique slug from a source field.

    Set `slug_source_field` on the model (e.g. 'title' or 'name').
    The slug field name defaults to `slug` but can be overridden by
    setting `slug_field_name` on the model.
    """

    slug_source_field: str = "title"
    slug_field_name: str = "slug"

    def _generate_base_slug(self, value: str) -> str:
        return slugify(value)[:240] or "item"

    def _ensure_unique_slug(self, base: str) -> str:
        Model = self.__class__
        candidate = base
        counter = 1
        lookup = {self.slug_field_name: candidate}
        pk = getattr(self, "pk", None)
        while Model.objects.filter(**lookup).exclude(pk=pk).exists():  # type: ignore
            candidate = f"{base}-{counter}"
            lookup = {self.slug_field_name: candidate}
            counter += 1
        return candidate

    def save(self, *args, **kwargs):
        # Only set slug if it's empty and source field exists
        current_slug = getattr(self, self.slug_field_name, None)
        source = getattr(self, self.slug_source_field, None)
        if (current_slug is None or current_slug == "") and source:
            base = self._generate_base_slug(str(source))
            unique = self._ensure_unique_slug(base)
            setattr(self, self.slug_field_name, unique)
        return super().save(*args, **kwargs)  # type: ignore


class Country(SlugMixin, models.Model):
    slug_source_field = "name"
    name = models.CharField(max_length=100)  # i18n en plantilla
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Service(SlugMixin, models.Model):
    slug_source_field = "title"
    title = models.CharField(max_length=255)  # traducible
    description = models.TextField()  # traducible
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ArticleCategory(SlugMixin, models.Model):
    slug_source_field = "name"
    name = models.CharField(max_length=150)  # traducible por i18n
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Article(SlugMixin, models.Model):
    slug_source_field = "title"
    title = models.CharField(max_length=255)  # traducible
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    content = RichTextField()  # traducible
    category = models.ForeignKey(
        ArticleCategory, on_delete=models.SET_NULL, null=True, blank=True
    )
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True
    )  # Artículos sobre un país
    publish = models.BooleanField(default=True)
    cover_image = models.ImageField(upload_to="articles/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Auto-generate a unique slug from title when not provided.

        The slug is limited to 240 chars for space to append counters.
        """
        if not self.slug and self.title:
            base = slugify(self.title)[:240] or "article"
            candidate = base
            counter = 1
            while Article.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base}-{counter}"
                counter += 1
            self.slug = candidate
        super().save(*args, **kwargs)


class InvestmentObject(models.Model):
    title = models.CharField(max_length=255)  # traducible
    description = models.TextField()  # traducible
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    expected_roi = models.DecimalField(max_digits=5, decimal_places=2)  # %
    active = models.BooleanField(default=True)
    images = models.JSONField(default=list, blank=True)  # URLs o rutas de imagen

    def __str__(self):
        return self.title


class LandingPage(SlugMixin, models.Model):
    slug = models.SlugField(unique=True)
    slug_source_field = "title"
    title = models.CharField(max_length=255)  # traducible
    content = RichTextField()  # traducible
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, blank=True
    )
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Lead(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    message = models.TextField()
    source = models.CharField(
        max_length=50, default="form"
    )  # landing / article / header…
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class LiveDataCache(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True)


class MetalPrice(models.Model):
    metal = models.CharField(
        max_length=30,
        choices=[
            ("gold", "Gold"),
            ("silver", "Silver"),
            ("platinum", "Platinum"),
        ],
    )
    price = models.DecimalField(max_digits=20, decimal_places=6)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ["-timestamp"]


class FuelPrice(models.Model):
    fuel_type = models.CharField(max_length=50, default="Fuel Platts")
    price = models.DecimalField(max_digits=20, decimal_places=6)
    currency = models.CharField(max_length=10, default="USD")
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ["-timestamp"]


class SocialPlatform(StrEnum):
    WHATSAPP = "whatsapp"
    FACEBOOK = "facebook"
    X = "x"
    INSTAGRAM = "instagram"
    TELEGRAM = "telegram"
    YOUTUBE = "youtube"


class SocialLink(models.Model):
    """Store social network links (WhatsApp, Facebook, X, Instagram, Telegram, YouTube).

    Fields are annotated for clarity and to follow project typing guidelines.
    """

    platform = models.CharField(
        max_length=20,
        choices=[
            (SocialPlatform.WHATSAPP, "WhatsApp"),
            (SocialPlatform.FACEBOOK, "Facebook"),
            (SocialPlatform.X, "X"),
            (SocialPlatform.INSTAGRAM, "Instagram"),
            (SocialPlatform.TELEGRAM, "Telegram"),
            (SocialPlatform.YOUTUBE, "YouTube"),
        ],
        default=SocialPlatform.WHATSAPP,
    )
    url = models.URLField(max_length=500)
    active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.platform} — {self.url}"

    class Meta:
        ordering = ["order", "platform"]
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
