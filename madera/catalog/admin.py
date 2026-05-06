from django.contrib import admin

from .models import Category
from .models import ExchangeRate
from .models import Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price_usd", "stock", "category", "is_published"]


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ["value_bolivares", "update_date"]
