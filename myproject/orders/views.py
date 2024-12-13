from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from myplatform.mixins import PlatformApiMixin
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductViewSet(PlatformApiMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(PlatformApiMixin, viewsets.ModelViewSet):
    queryset = Order.objects.select_related('customer', 'seller') \
                            .prefetch_related('products')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['products__name']
    filterset_fields = ['customer__user', 'seller__user']
    ordering_fields = ['amount']
