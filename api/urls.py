from django.urls import path, include
from .yasg import urlpatterns as url_doc

from rest_framework.routers import DefaultRouter

from app.views import (
    WarehouseViewSet, ProductViewSet, HistoryViewSet,
    HistoryProductViewSet, CurrencyViewSet
)

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet)
router.register(r'products', ProductViewSet)
router.register(r'histories', HistoryViewSet)
router.register(r'history-products', HistoryProductViewSet)
router.register(r'currencies', CurrencyViewSet)


urlpatterns = [
    # path('auth/', include('api.auth.urls')),

    path('', include(router.urls))
]

urlpatterns += url_doc