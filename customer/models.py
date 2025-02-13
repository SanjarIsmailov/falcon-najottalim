from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)  # Customer's first name
    last_name = models.CharField(max_length=100)  # Customer's last name
    email = models.EmailField(unique=True)  # Customer's email (unique)
    phone = models.CharField(max_length=20, blank=True, null=True)  # Phone number
    billing_address = models.TextField(blank=True, null=True)  # Billing address
    joined_date = models.DateField()  # Date the customer joined

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
