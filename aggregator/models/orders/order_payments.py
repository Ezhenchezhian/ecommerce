from django.contrib.postgres.fields import ArrayField
from django.db import models

from aggregator.models.orders.order_details import OrderDetail


class OrderPayment(models.Model):
    entity_id = models.BigIntegerField()
    account_status = models.IntegerField(null=True)
    additional_information = ArrayField(models.TextField(), blank=True, size=255)
    amount_ordered = models.FloatField()
    base_amount_ordered = models.FloatField()
    base_shipping_amount = models.FloatField()
    cc_exp_year = models.CharField(max_length=10)
    cc_last4 = models.CharField(max_length=25, null=True)
    cc_ss_start_month = models.CharField(max_length=10)
    cc_ss_start_year = models.CharField(max_length=10)
    method = models.CharField(max_length=10)
    shipping_amount = models.FloatField()
    parent_id = models.ForeignKey(OrderDetail, on_delete=models.PROTECT, related_name='payment')

    class Meta:
        db_table = 'order_payments'
