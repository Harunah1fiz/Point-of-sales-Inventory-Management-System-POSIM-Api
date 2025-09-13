from rest_framework import serializers
from .models import InventoryTransaction

class InventoryTransactionSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    user_name = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = InventoryTransaction
        fields = ['id', 'product', 'product_name', 'action_type','quantity', 'note', 'user_name', 'created_at']
        read_only_fields = ["created_at"]