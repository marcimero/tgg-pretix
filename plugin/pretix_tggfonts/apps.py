from django.apps import AppConfig

from . import __version__


class PluginApp(AppConfig):
    name = "pretix_tggfonts"
    verbose_name = "TGG Fonts & Theme"

    class PretixPluginMeta:
        name = "TGG Fonts & Theme"
        author = "The GOAT Germany"
        description = (
            "Inter, Geist, Saira, Saira Condensed and Saira Semi Condensed "
            "for ticket PDFs and the shop, plus custom shop CSS (custom.css)"
        )
        # visible so the custom CSS can be enabled per event; the fonts are
        # registered globally either way (plain signal, not event-scoped).
        visible = True
        version = __version__
        compatibility = "pretix>=2024.7.0"

    def ready(self):
        from . import signals  # NOQA
