from django.db import models

from aggregator.models.orders.order_details import OrderDetail


class OrderStatusHistory(models.Model):
    entity_id = models.BigIntegerField()
    comment = models.TextField(null=True)
    entity_name = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    is_customer_notified = models.IntegerField(null=True)
    is_visible_on_front = models.IntegerField(null=True)
    status = models.TextField(null=True)
    parent_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'order_status_histories'
