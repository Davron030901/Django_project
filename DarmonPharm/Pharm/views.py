from rest_framework import viewsets
from .models import Product, Supplier, Warehouse, WarehouseOrder
from .serializers import ProductSerializer, SupplierSerializer, WarehouseSerializer, WarehouseOrderSerializer
from rest_framework.authentication import SessionAuthentication


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    authentication_classes = [SessionAuthentication]


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    authentication_classes = [SessionAuthentication]


class WarehouseOrderViewSet(viewsets.ModelViewSet):
    queryset = WarehouseOrder.objects.all()
    serializer_class = WarehouseOrderSerializer
    authentication_classes = [SessionAuthentication]


