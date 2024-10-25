from rest_framework import serializers
from .models import Warehouse, Product, History, HistoryProduct, Currency


class WarehouseSerializer(serializers.ModelSerializer):
    goods_quantity = serializers.ReadOnlyField()

    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'owner', 'goods_quantity', 'created_date']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'quantity', 'warehouse', 'image', 'expiration_date',
            'cost_price', 'sell_price', 'code', 'amount_type', 'cost_currency',
            'sell_currency', 'deliver_date', 'created_date'
        ]


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = [
            'id', 'user_id', 'buyer_name', 'debt_return_date', 'debt_currency',
            'debt_amount', 'created_date'
        ]


class HistoryProductSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = HistoryProduct
        fields = [
            'id', 'quantity', 'amount_type', 'code', 'product', 'sold_price',
            'sold_currency', 'name'
        ]


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name', 'ru_name', 'created_date']
