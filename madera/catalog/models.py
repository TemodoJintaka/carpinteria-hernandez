from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productos/')
    is_published = models.BooleanField(default=True)

class ExchangeRate(models.Model):
    value_bolivares = models.DecimalField(max_digits=10, decimal_places=2)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Tasa de Cambio"