from rest_framework import serializers

from aggregator.models import OrderDetail, OrderItem, OrderStatusHistory, OrderBillingAddress, OrderPayment


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusHistory
        fields = '__all__'


class OrderBillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBillingAddress
        fields = '__all__'


class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPayment
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'
