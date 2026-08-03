from django.dispatch import receiver
from django.templatetags.static import static
from django.utils.safestring import mark_safe
from pretix.plugins.ticketoutputpdf.signals import register_fonts
from pretix.presale.signals import html_head

BASE = "pretix_tggfonts"


# Shop CSS: injected into <head> of all presale pages of events that have
# this plugin enabled (Einstellungen → Plugins). Edit static/pretix_tggfonts/
# custom.css, push, redeploy. The fonts below work regardless of activation.
@receiver(html_head, dispatch_uid="tgg_custom_css")
def tgg_custom_css(sender, request=None, **kwargs):
    return mark_safe(
        f'<link rel="stylesheet" href="{static(f"{BASE}/custom.css")}">'
    )


def _style(name):
    return {
        "truetype": f"{BASE}/{name}.ttf",
        "woff2": f"{BASE}/{name}.woff2",
    }


@receiver(register_fonts, dispatch_uid="tgg_fonts")
def tgg_fonts(sender, **kwargs):
    return {
        "Inter": {
            "regular": _style("Inter-Regular"),
            "bold": _style("Inter-Bold"),
            "italic": _style("Inter-Italic"),
            "bolditalic": _style("Inter-BoldItalic"),
        },
        "Geist": {
            "regular": _style("Geist-Regular"),
            "bold": _style("Geist-Bold"),
            "italic": _style("Geist-Italic"),
            "bolditalic": _style("Geist-BoldItalic"),
        },
        "Saira": {
            "regular": _style("Saira-Regular"),
            "bold": _style("Saira-Bold"),
            "italic": _style("Saira-Italic"),
            "bolditalic": _style("Saira-BoldItalic"),
        },
        # Saira Condensed / Semi Condensed ship no italics on Google Fonts —
        # map italic styles to the uprights (same approach as pretix-fontpack-free).
        "Saira Condensed": {
            "regular": _style("SairaCondensed-Regular"),
            "bold": _style("SairaCondensed-Bold"),
            "italic": _style("SairaCondensed-Regular"),
            "bolditalic": _style("SairaCondensed-Bold"),
        },
        "Saira Semi Condensed": {
            "regular": _style("SairaSemiCondensed-Regular"),
            "bold": _style("SairaSemiCondensed-Bold"),
            "italic": _style("SairaSemiCondensed-Regular"),
            "bolditalic": _style("SairaSemiCondensed-Bold"),
        },
    }
