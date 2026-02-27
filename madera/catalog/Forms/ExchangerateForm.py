from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import ExchangeRate

class ExchangeRateForm(forms.ModelForm):
    class Meta:
        model = ExchangeRate
        fields = ["value_bolivares"]
        labels = {
            "value_bolivares": _("Valor en bolivares"),
        }