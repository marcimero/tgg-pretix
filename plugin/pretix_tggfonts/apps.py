from django.apps import AppConfig

from . import __version__


class PluginApp(AppConfig):
    name = "pretix_tggfonts"
    verbose_name = "TGG Fonts"

    class PretixPluginMeta:
        name = "TGG Fonts"
        author = "The GOAT Germany"
        description = (
            "Inter, Geist, Saira, Saira Condensed and Saira Semi Condensed "
            "for ticket PDFs and the shop"
        )
        # Fonts are registered globally (plain signal, not event-scoped),
        # so there is nothing to enable per event — hide the plugin.
        visible = False
        version = __version__
        compatibility = "pretix>=2024.7.0"

    def ready(self):
        from . import signals  # NOQA
