from django.contrib.postgres.fields import ArrayField
from django.db import models

from aggregator.models.orders.order_details import OrderDetail


class OrderPayment(models.Model):
    entity_id = models.BigIntegerField()
    account_status = models.IntegerField(null=True)
    additional_information = ArrayField(models.TextField(), blank=True, size=255, null=True)
    amount_ordered = models.FloatField(null=True)
    amount_authorized = models.FloatField(null=True)
    amount_paid = models.FloatField(null=True)
    amount_refunded = models.FloatField(null=True)
    base_amount_ordered = models.FloatField(null=True)
    base_amount_paid = models.FloatField(null=True)
    base_amount_paid_online = models.FloatField(null=True)
    base_amount_refunded = models.FloatField(null=True)
    base_amount_refunded_online = models.FloatField(null=True)
    base_shipping_amount = models.FloatField(null=True)
    base_shipping_captured = models.FloatField(null=True)
    base_shipping_refunded = models.FloatField(null=True)
    cc_exp_year = models.CharField(max_length=255,null=True)
    cc_last4 = models.CharField(max_length=255, null=True)
    last_trans_id = models.CharField(max_length=255, null=True)
    cc_ss_start_month = models.CharField(max_length=255,null=True)
    cc_ss_start_year = models.CharField(max_length=255, null=True)
    method = models.CharField(max_length=255)
    shipping_amount = models.FloatField(null=True)
    shipping_captured = models.FloatField(null=True)
    shipping_refunded = models.FloatField(null=True)
    parent_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'order_payments'
