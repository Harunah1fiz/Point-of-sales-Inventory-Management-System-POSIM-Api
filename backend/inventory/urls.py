from django.urls import path
from . import views

urlpatterns = [
    path("", views.InventoryTransactionListCreateAPIView.as_view(), name="inventory-list-create"),
]
