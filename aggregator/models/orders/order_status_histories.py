from django.db import models

from aggregator.models.orders.order_details import OrderDetail


class OrderStatusHistory(models.Model):
    entity_id = models.BigIntegerField()
    comment = models.TextField()
    entity_name = models.TextField()
    created_at = models.DateTimeField()
    is_customer_notified = models.IntegerField()
    is_visible_on_front = models.IntegerField()
    status = models.TextField()
    parent_id = models.ForeignKey(OrderDetail, on_delete=models.PROTECT, related_name='status_histories')

    class Meta:
        db_table = 'order_status_histories'
