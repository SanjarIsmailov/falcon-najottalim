from django.contrib import admin
from django.utils.html import format_html
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "formatted_price", "stock_status", "rating", "is_new", "admin_image")
    list_filter = ("stock_status", "is_new", "rating")
    search_fields = ("name", "description", "stock_status")
    ordering = ("-id",)

    def formatted_price(self, obj):
        return format_html(
            '<span style="text-decoration: line-through; color: red;">${}</span> <strong style="color: green;">${}</strong>',
            obj.original_price or 0, obj.price or 0
        )
    formatted_price.short_description = "Price"

    def admin_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;" />', obj.image.url)
        return "No Image"
    admin_image.short_description = "Image"