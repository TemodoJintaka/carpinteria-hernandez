from django import forms
from madera.ventas.models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['lead', 'product', 'price', 'quantity', 'status']