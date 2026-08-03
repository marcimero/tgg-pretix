from django.dispatch import receiver
from pretix.plugins.ticketoutputpdf.signals import register_fonts

BASE = "pretix_tggfonts"


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
