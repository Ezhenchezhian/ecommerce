from django.db import models

from aggregator.models.orders.order_details import OrderDetail


class OrderItem(models.Model):
    applied_rule_ids = models.CharField(max_length=255, null=True)
    amount_refunded = models.FloatField(null=True)
    base_amount_refunded = models.FloatField(null=True)
    base_discount_amount = models.FloatField(null=True)
    base_discount_invoiced = models.FloatField(null=True)
    base_discount_refunded = models.FloatField(null=True)
    base_discount_tax_compensation_amount = models.FloatField(null=True)
    base_discount_tax_compensation_invoiced = models.IntegerField(null=True)
    base_discount_tax_compensation_refunded = models.IntegerField(null=True)
    base_original_price = models.FloatField(null=True)
    base_price = models.FloatField(null=True)
    base_price_incl_tax = models.FloatField(null=True)
    base_row_invoiced = models.FloatField(null=True)
    base_row_total = models.FloatField(null=True)
    base_row_total_incl_tax = models.FloatField(null=True)
    base_tax_amount = models.FloatField(null=True)
    base_tax_invoiced = models.IntegerField(null=True)
    base_tax_refunded = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    discount_amount = models.FloatField(null=True)
    discount_invoiced = models.IntegerField(null=True)
    discount_refunded = models.IntegerField(null=True)
    discount_percent = models.FloatField(null=True)
    free_shipping = models.IntegerField(null=True)
    discount_tax_compensation_amount = models.FloatField(null=True)
    discount_tax_compensation_invoiced = models.IntegerField(null=True)
    discount_tax_compensation_refunded = models.IntegerField(null=True)
    discount_tax_compensation_canceled = models.FloatField(null=True)
    is_qty_decimal = models.IntegerField(null=True)
    is_virtual = models.IntegerField(null=True)
    item_id = models.IntegerField(null=True)
    name = models.TextField(null=True)
    no_discount = models.IntegerField(null=True)
    order_id = models.IntegerField(null=True)
    original_price = models.FloatField(null=True)
    price = models.FloatField(null=True)
    price_incl_tax = models.FloatField(null=True)
    product_id = models.BigIntegerField(null=True)
    product_type = models.TextField(null=True)
    qty_canceled = models.IntegerField(null=True)
    qty_invoiced = models.IntegerField(null=True)
    qty_ordered = models.IntegerField(null=True)
    qty_refunded = models.IntegerField(null=True)
    qty_shipped = models.IntegerField(null=True)
    quote_item_id = models.BigIntegerField(null=True)
    row_invoiced = models.IntegerField(null=True)
    row_total = models.FloatField(null=True)
    row_total_incl_tax = models.IntegerField(null=True)
    row_weight = models.IntegerField(null=True)
    sku = models.TextField(null=True)
    weee_tax_applied = models.TextField(null=True)
    store_id = models.BigIntegerField(null=True)
    tax_amount = models.FloatField(null=True)
    tax_invoiced = models.IntegerField(null=True)
    tax_percent = models.FloatField(null=True)
    tax_refunded = models.FloatField(null=True)
    updated_at = models.DateTimeField(null=True)
    weight = models.FloatField(null=True)
    parent_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'order_items'
