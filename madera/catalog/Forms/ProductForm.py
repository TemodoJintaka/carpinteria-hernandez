from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price_usd", "stock", "category", "image", "is_published","description"]
        labels = {
            "name": _("Nombre"),
            "description": _("Descripción"),
            "price_usd": _("Precio USD"),
            "stock": _("Stock"),
            "category": _("Categoría"),
            "image": _("Imagen"),
            "is_published": _("Publicado"),
        }
        widgets = {
            "category": forms.Select(attrs={"class": "form-control select-as-input"}),
            "is_published": forms.CheckboxInput(attrs={"class": "custom-control-input"}),
        }