from django.contrib import admin

from .models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("id", "vehicle", "user", "quantity", "purchase_price", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("vehicle__make", "vehicle__model", "user__username", "user__email")
    readonly_fields = ("created_at",)
