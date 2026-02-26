from django.contrib import admin

# Register your models here.
from .models import Lead
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'whatsapp', 'product_interest', 'message', 'created_at']