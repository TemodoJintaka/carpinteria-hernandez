from django.urls import path

app_name = "landing"


def get_urlpatterns():
    from madera.web.views import LandingCatalogView, LandingPageView

    return [
        path("", LandingPageView.as_view(), name="landing"),
        path("catalogo/", LandingCatalogView.as_view(), name="catalog"),
    ]


urlpatterns = get_urlpatterns()