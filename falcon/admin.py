import csv
from django.http import HttpResponse
from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Avg, Sum
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "formatted_price", "stock_status", "average_rating", "total_stock", "is_new", "admin_image")
    list_filter = ("stock_status", "is_new", "rating")
    search_fields = ("name", "description", "stock_status")
    ordering = ("-id",)
    actions = ["export_as_csv"]  # ✅ Add export action

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(
            avg_rating=Avg("rating"),
            total_stock=Sum("stock")
        )

    def formatted_price(self, obj):
        return format_html(
            '<span style="text-decoration: line-through; color: red;">${}</span> <strong class="text-success">${}</strong>',
            obj.original_price or 0, obj.price or 0
        )

    formatted_price.short_description = "Price"

    def average_rating(self, obj):
        return round(obj.avg_rating, 2) if obj.avg_rating else "No Rating"

    average_rating.short_description = "Avg Rating"

    def total_stock(self, obj):
        return obj.total_stock or 0

    total_stock.short_description = "Total Stock"

    def admin_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;" />', obj.image.url)
        return "No Image"

    admin_image.short_description = "Image"

    # ✅ Export to CSV function
    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="products.csv"'

        writer = csv.writer(response)
        writer.writerow(["ID", "Name", "Price", "Stock Status", "Average Rating", "Total Stock"])

        for product in queryset:
            writer.writerow([
                product.id,
                product.name,
                product.price,
                product.stock_status,
                round(product.avg_rating, 2) if hasattr(product, "avg_rating") else "N/A",
                product.total_stock if hasattr(product, "total_stock") else 0
            ])

        return response

    export_as_csv.short_description = "Export Selected as CSV"