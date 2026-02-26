from django.db import models

from madera.catalog.models import Product

class Lead(models.Model):
    client_name = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    # Relacionamos el lead con el producto que le gustó
    product_interest = models.ManyToManyField('catalog.Product', on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
