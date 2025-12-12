from django.apps import AppConfig


class AppConfig(AppConfig):
    name = "app"

    def ready(self):
        """Import translation registration early to avoid NotRegistered errors.

        The import triggers the modeltranslation registration for models and
        ensures translation fields are available before admin or other modules
        attempt to access them.
        """
        try:
            # Import translation module to register translation fields
            from . import translation  # noqa: F401
        except ImportError:
            # If translations cannot be imported (e.g. tests running in partial env),
            # allow the app to still initialize; the import error will be surfaced
            # when translations are actually required.
            pass
