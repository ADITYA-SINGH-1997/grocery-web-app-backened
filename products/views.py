from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import ProductSerializer, CategorySerializer
from products.models import Product, Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny, ]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ProductSerializer
    lookup_field = "slug"

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["category__name", "name", "description"]
