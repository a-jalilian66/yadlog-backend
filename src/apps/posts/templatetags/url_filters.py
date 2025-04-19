from django import template
from urllib.parse import unquote

register = template.Library()


@register.filter
def urlunquote(value):
    """
    Decode a percent-encoded URL to human-readable form.
    Example: /blog/%D8%A2%D8%B4%D9%86%D8%A7%DB%8C%DB%8C → /blog/آشنايی
    """
    return unquote(value)
