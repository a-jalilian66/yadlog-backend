from django.utils.translation import pgettext_lazy
from django.utils.translation import gettext_lazy as _


def main_menu(request):
    return {
        "menu_items": [
            {"title": pgettext_lazy("menu", "Home"), "url": "posts:home"},
            {"title": pgettext_lazy("menu", "Categories"), "url": "posts:home"},
            {"title": pgettext_lazy("menu", "About Me"), "url": "posts:home"},
        ]
    }


def site_info(request):
    return {
        "site_info": {
            "title": "Yadlog",
            'description': _("I write what I learn - from little tips to in‑depth technical experiences."),
            "tagline": _("Learn. Share. Code."),
            "links": {
                "github": "https://github.com/a-jalilian66",
            }
        }
    }
