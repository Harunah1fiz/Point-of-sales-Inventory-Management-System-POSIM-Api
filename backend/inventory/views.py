from rest_framework import generics, permissions, authentication
from .models import InventoryTransaction
from .serializers import InventoryTransactionSerializer

class InventoryTransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = InventoryTransaction.objects.all()
    serializer_class = InventoryTransactionSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [authentication.SessionAuthentication]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # log the user who did it
