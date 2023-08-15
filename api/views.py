import django_filters as filters
from rest_framework import viewsets
from store.models import *
from accounts.models import *
from .serializers import *


class ProductFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name='category')

    class Meta:
        model = Product
        fields = ['category']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class ShopperViewSet(viewsets.ModelViewSet):
    queryset = Shopper.objects.all()
    serializer_class = ShopperSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
