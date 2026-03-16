from django.db import models
from django.core.exceptions import ValidationError
from django.db import transaction
from madera.catalog.models import Product


class Lead(models.Model):
    client_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    # Relacionamos el lead con el producto que le gustó
    product_interest = models.ManyToManyField('catalog.Product', blank=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name


class SaleStatus(models.TextChoices):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'
    DELIVERED = 'delivered'

    def __str__(self):
        return self.name

class Sale(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=SaleStatus.choices, default=SaleStatus.PENDING)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    from django.core.exceptions import ValidationError
    from django.db import transaction

    def save(self, *args, **kwargs):
        # 1. Calculamos el total automáticamente: $Total = Precio \times Cantidad$
        self.total = self.price * self.quantity

        # 2. Lógica de Stock (Solo si la venta es nueva y confirmada)
        if not self.pk and self.status == SaleStatus.CONFIRMED: # Si la venta es nueva y confirmada
            if self.product.stock < self.quantity: # Si el stock es menor a la cantidad
                raise ValidationError(f"No hay suficiente stock. Disponible: {self.product.stock}")

            # Usamos una transacción atómica para asegurar integridad
            with transaction.atomic():
                self.product.stock -= self.quantity # Restamos la cantidad de la venta al stock del producto
                self.product.save() # Guardamos el producto

        super().save(*args, **kwargs) # Guardamos la venta

    def __str__(self):
        return f"{self.lead.client_name} - {self.product.name}"
