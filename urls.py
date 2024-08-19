from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from . import views

admin.autodiscover()

urlpatterns = [
        path('booking_discovery_session', views.index, name="booking_discovery_session"),
]


