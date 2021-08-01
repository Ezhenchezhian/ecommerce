from django.urls import path, include
from rest_framework.routers import DefaultRouter

from aggregator.views import OrderDetailModelViewSet, OrderStatusHistoryModelViewSet, OrderPaymentModelViewSet, \
    OrderBillAddressModelViewSet, OrderItemModelViewSet

router = DefaultRouter()
router.register('detail', OrderDetailModelViewSet, basename='Order Details')
router.register('status', OrderStatusHistoryModelViewSet, basename='Order Status History')
router.register('payment', OrderPaymentModelViewSet, basename='Order Payments')
router.register('address', OrderBillAddressModelViewSet, basename='Order Billing Address')
router.register('items', OrderItemModelViewSet, basename='Order Items')
urlpatterns = [
    path('orders/', include(router.urls))
]
