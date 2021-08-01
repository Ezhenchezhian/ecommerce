from rest_framework.viewsets import ModelViewSet

from aggregator.models import OrderDetail, OrderBillingAddress, OrderPayment, OrderStatusHistory, OrderItem
from aggregator.serializers import OrderDetailSerializer, OrderBillingAddressSerializer, OrderItemSerializer, \
    OrderPaymentSerializer, OrderStatusHistorySerializer


class OrderDetailModelViewSet(ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    lookup_field = 'entity_id'
    filterset_fields = ['status']


class OrderBillAddressModelViewSet(ModelViewSet):
    queryset = OrderBillingAddress.objects.all()
    serializer_class = OrderBillingAddressSerializer
    lookup_field = 'entity_id'


class OrderPaymentModelViewSet(ModelViewSet):
    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer
    lookup_field = 'entity_id'


class OrderStatusHistoryModelViewSet(ModelViewSet):
    queryset = OrderStatusHistory.objects.all()
    serializer_class = OrderStatusHistorySerializer
    lookup_field = 'entity_id'


class OrderItemModelViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = 'entity_id'
