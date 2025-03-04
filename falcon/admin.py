import csv
from django.http import HttpResponse
from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Avg
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "formatted_price", "stock_status", "average_rating", "is_new", "admin_image")
    list_filter = ("stock_status", "is_new")
    search_fields = ("name", "description")
    ordering = ("-id",)
    actions = ["export_as_csv"]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(avg_rating=Avg("rating"))

    def formatted_price(self, obj):
        return format_html(
            '<span style="text-decoration: line-through; color: red;">${}</span> <strong style="color: green;">${}</strong>',
            obj.original_price or 0, obj.price or 0
        )

    formatted_price.short_description = "Price"

    def average_rating(self, obj):
        return round(obj.avg_rating, 2) if obj.avg_rating else "No Rating"

    average_rating.short_description = "Avg Rating"

    def admin_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;" />', obj.image.url) if obj.image else "No Image"

    admin_image.short_description = "Image"

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="products.csv"'

        writer = csv.writer(response)
        writer.writerow(["ID", "Name", "Price", "Stock Status", "Average Rating"])

        for product in queryset:
            writer.writerow([
                product.id,
                product.name,
                product.price,
                product.stock_status,
                round(product.avg_rating, 2) if hasattr(product, "avg_rating") else "N/A"
            ])

        return response

    export_as_csv.short_description = "Export Selected as CSV"
