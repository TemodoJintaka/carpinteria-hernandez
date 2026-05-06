from django.urls import path

from madera.web.views import LandingCatalogView
from madera.web.views import LandingPageView

app_name = "landing"

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing"),
    path("catalogo/", LandingCatalogView.as_view(), name="catalog"),
]
