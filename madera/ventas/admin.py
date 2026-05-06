from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ["client_name", "whatsapp", "product_count", "message", "created_at"]

    @admin.display(description="Products")
    def product_count(self, obj):
        return obj.product_interest.count()
