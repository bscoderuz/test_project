from rest_framework import generics
from apps.product.models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


__all__ = ["ProductListCreateView", "ProductRetrieveUpdateDestroyView"]
