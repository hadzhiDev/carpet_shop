from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Warehouse, Product, History, HistoryProduct, Currency
from .serializers import WarehouseSerializer, ProductSerializer, HistorySerializer, HistoryProductSerializer, CurrencySerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    """
    Viewset for Warehouse
    """
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """
    Viewset for Product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class HistoryViewSet(viewsets.ModelViewSet):
    """
    Viewset for History
    """
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [IsAuthenticated]


class HistoryProductViewSet(viewsets.ModelViewSet):
    """
    Viewset for HistoryProduct
    """
    queryset = HistoryProduct.objects.all()
    serializer_class = HistoryProductSerializer
    permission_classes = [IsAuthenticated]


class CurrencyViewSet(viewsets.ModelViewSet):
    """
    Viewset for Currency
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]
