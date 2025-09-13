from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import InventoryTransaction

@receiver(post_save, sender = InventoryTransaction)
def update_product_stock(sender, instance, created, **kwargs):
    print("hello")
    if created:
        product = instance.product
        if instance.action_type == "ADD":
            product.stock_quantity += instance.quantity
        elif instance.action_type == "OUT":
            product.stock_quantity -= instance.quantity
        product.save()
