from django.shortcuts import render
from rest_framework import authentication, permissions, generics
from rest_framework.exceptions import NotFound
from .serializers import ProductSerializer
from  .models import Product
# Create your views here.

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def get_object(self):
        queryset = self.get_queryset()
        lookup_value = self.kwargs.get("lookup")

        try:
            return queryset.get(slug=lookup_value)
        except Product.DoesNotExist:
            pass

        try:
            return queryset.get(id=lookup_value)
        except Product.DoesNotExist:
            raise NotFound("Product not found")
        

class ProductByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        lookup_value = self.kwargs.get("category")
        return Product.objects.filter(category=lookup_value)


