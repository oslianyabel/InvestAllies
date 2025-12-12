from django.test import TestCase
from django.utils.text import slugify

from .models import Article, ArticleCategory, Country


class SlugTranslationTests(TestCase):
    def test_article_translated_slugs_generated(self):
        cat = ArticleCategory.objects.create(name="General", slug="general")
        country = Country.objects.create(name="Testland", slug="testland")
        a = Article.objects.create(
            title="My English Title",
            category=cat,
            country=country,
            content="Hello",
            publish=True,
        )
        # set translated titles (simulate modeltranslation behavior)
        setattr(a, "title_es", "Mi Título Español")
        setattr(a, "title_fr", "Mon Titre Français")
        # clear the translated slugs in case setup has values
        setattr(a, "slug_es", "")
        setattr(a, "slug_fr", "")
        a.save()

        self.assertEqual(getattr(a, "slug_es"), slugify("Mi Título Español"))
        self.assertEqual(getattr(a, "slug_fr"), slugify("Mon Titre Français"))
