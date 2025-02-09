from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    original_price = models.FloatField(blank=True, null=True)  # Allow null values
    price = models.FloatField(blank=True, null=True)  # Allow null values
    rating = models.FloatField(blank=True, null=True)
    reviews_count = models.IntegerField(default=0)
    shipping_cost = models.FloatField(default=0)
    stock_status = models.CharField(max_length=50, default="Available")
    is_new = models.BooleanField(default=False)
    specifications = models.JSONField(default=dict, blank=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)  # Image field for the product photo

    def __str__(self):
        return self.name

    @property
    def discount_percentage(self):
        """Compute discount percentage safely, avoiding NoneType errors."""
        if self.original_price and self.price:  # Check for None values
            if self.original_price > self.price:
                return round((self.original_price - self.price) / self.original_price * 100, 2)
        return 0.0  # Return 0 if values are missing