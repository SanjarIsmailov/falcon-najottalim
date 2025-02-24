from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Product
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Product)
def log_product_creation(sender, instance, created, **kwargs):
    if created:
        logger.info(f"New product added: {instance.name} (Price: ${instance.price})")


@receiver(pre_save, sender=Product)
def track_price_changes(sender, instance, **kwargs):
    if instance.pk:  # Check if the product already exists
        old_product = Product.objects.get(pk=instance.pk)
        if old_product.price != instance.price:
            logger.info(f"Price changed for {instance.name}: ${old_product.price} -> ${instance.price}")


@receiver(pre_save, sender=Product)
def notify_out_of_stock(sender, instance, **kwargs):
    if instance.pk:
        old_product = Product.objects.get(pk=instance.pk)
        if old_product.stock_status != instance.stock_status and instance.stock_status.lower() == "out of stock":
            logger.warning(f"Product '{instance.name}' is now out of stock!")
