from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = "landing/index.html"


class LandingCatalogView(TemplateView):
    """
    Vista sencilla solo para renderizar el catálogo de la landing.
    Más adelante se puede reemplazar el contenido estático del template
    por productos reales y categorías desde la base de datos.
    """

    template_name = "landing/catalog.html"
