from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
# Create your models here.

User = get_user_model()

class InventoryTransaction(models.Model):
    INVENTORY_ACTION = (
        ("ADD", "Added Stock"),
        ("OUT",  "Stock Out")
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="inventory_product")
    action_type = models.CharField(max_length=5,  choices=INVENTORY_ACTION)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    note = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.action_type} - {self.product.name} ({self.quantity})"
