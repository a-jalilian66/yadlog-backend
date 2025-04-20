from django.http import HttpResponse
from django.urls import reverse


def robots_txt(request):
    scheme = 'https' if request.is_secure() else 'http'
    host = request.get_host()
    sitemap_url = f"{scheme}://{host}{reverse('django.contrib.sitemaps.views.sitemap')}"
    lines = [
        "User-agent: *",
        "Disallow: /static/",
        "Disallow: /media/",
        "Allow: /",
        f"Sitemap: {sitemap_url}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
