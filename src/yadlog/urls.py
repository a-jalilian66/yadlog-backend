"""yadlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap

from apps.common.sitemaps import PostSiteMap, StaticSitemap, TagSitemap, CategorySitemap
from apps.common.views import robots_txt

sitemaps = {
    'posts': PostSiteMap,
    'categories': CategorySitemap,
    'tags': TagSitemap,
    'static': StaticSitemap
}

urlpatterns = [
    path('robots.txt', robots_txt),
    path('i18n/', include('django.conf.urls.i18n')),  # To change language
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('apps.posts.urls', namespace='posts')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    prefix_default_language=settings.PREFIX_DEFAULT_LANGUAGE
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
