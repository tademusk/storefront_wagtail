from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from algoliasearch_django import raw_index

from .models import Product

@receiver(post_save, sender=Product)
def update_index(sender, instance, **kwargs):
    raw_index.save_object(instance)

@receiver(post_delete, sender=Product)
def delete_from_index(sender, instance, **kwargs):
    raw_index.delete_object(instance)
