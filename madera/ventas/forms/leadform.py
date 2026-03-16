from django import forms
from madera.ventas.models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['client_name', 'email', 'whatsapp', 'message']