from django.db import models
from ckeditor.fields import RichTextField


class Country(models.Model):
    name = models.CharField(max_length=100)  # i18n en plantilla
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=255)  # traducible
    description = models.TextField()  # traducible
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ArticleCategory(models.Model):
    name = models.CharField(max_length=150)  # traducible por i18n
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)  # traducible
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


class LandingPage(models.Model):
    slug = models.SlugField(unique=True)
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
