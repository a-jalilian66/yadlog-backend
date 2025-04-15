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
        "site_title": "Yadlog",
        "site_tagline": _("Learn. Share. Code."),
        "social_links": {
            "github": "https://github.com/a-jalilian66",
        }
    }
