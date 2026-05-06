from django.db import models


class Lead(models.Model):
    client_name = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    # Relacionamos el lead con el producto que le gustó
    product_interest = models.ManyToManyField("catalog.Product", blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.client_name
