from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Customer
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Customer)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = "Welcome to Our Store!"
        message = f"Hello {instance.first_name},\n\nThank you for joining us! We’re excited to have you."
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [instance.email]

        send_mail(subject, message, from_email, recipient_list)
        logger.info(f"Welcome email sent to {instance.email}")


@receiver(post_delete, sender=Customer)
def log_customer_deletion(sender, instance, **kwargs):
    logger.warning(f"Customer {instance.first_name} {instance.last_name} (Email: {instance.email}) was deleted.")
