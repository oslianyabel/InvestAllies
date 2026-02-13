import os

import django

# Configuración del entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "InvestAllies.settings")
django.setup()

from app.models import Country


def run():
    country, created = Country.objects.get_or_create(
        slug="marruecos", defaults={"name": "Marruecos", "active": True}
    )
    if created:
        print(f"País '{country.name}' creado exitosamente.")
    else:
        print(f"El país '{country.name}' ya existe.")


if __name__ == "__main__":
    run()
