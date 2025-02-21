from django.contrib import admin

from customer.models import Customer


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "joined_date")
    list_filter = ("joined_date",)
    search_fields = ("first_name", "last_name", "email", "phone")
    fieldsets = (
        (None, {
            "fields": ("first_name", "last_name", "email", "phone")
        }),
        ("Address", {
            "fields": ("billing_address",),
        }),
        ("Other Information", {
            "fields": ("joined_date",),
        }),
    )
