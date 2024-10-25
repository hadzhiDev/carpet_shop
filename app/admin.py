from django.contrib import admin
from .models import Warehouse, Product, History, HistoryProduct, Currency


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'goods_quantity', 'created_date')
    search_fields = ('name',)
    ordering = ('-created_date',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('products')  # Optimizes goods_quantity calculation
        return queryset


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'warehouse', 'sell_price', 'cost_price', 'expiration_date', 'deliver_date')
    search_fields = ('name', 'code')
    list_filter = ('warehouse', 'expiration_date', 'deliver_date')
    ordering = ('-created_date',)


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('buyer_name', 'user_id', 'created_date')
    search_fields = ('buyer_name', 'user_id__name')
    ordering = ('-created_date',)


@admin.register(HistoryProduct)
class HistoryProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'quantity', 'amount_type')
    search_fields = ('code',)


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'ru_name')
    search_fields = ('name', 'ru_name')

