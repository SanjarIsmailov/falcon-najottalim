from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    original_price = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    reviews_count = models.IntegerField(default=0)
    shipping_cost = models.FloatField(default=0)
    stock_status = models.CharField(max_length=50, default="Available")
    is_new = models.BooleanField(default=False)
    specifications = models.JSONField(default=dict, blank=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def discount_percentage(self):
        if self.original_price and self.price:
            if self.original_price > self.price:
                return round((self.original_price - self.price) / self.original_price * 100, 2)
        return 0.0