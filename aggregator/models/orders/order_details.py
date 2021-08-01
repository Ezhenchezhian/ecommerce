from django.db import models


class OrderDetail(models.Model):
    entity_id = models.BigIntegerField()
    base_currency_code = models.CharField(max_length=10)
    base_discount_amount = models.FloatField()
    base_grand_total = models.FloatField()
    base_discount_tax_compensation_amount = models.FloatField()
    base_shipping_amount = models.FloatField()
    base_shipping_discount_amount = models.FloatField()
    base_shipping_discount_tax_compensation_amnt = models.FloatField()
    base_shipping_incl_tax = models.FloatField()
    base_shipping_tax_amount = models.FloatField()
    base_subtotal = models.FloatField()
    base_subtotal_incl_tax = models.FloatField()
    base_tax_amount = models.FloatField()
    base_total_due = models.FloatField()
    base_to_global_rate = models.FloatField()
    base_to_order_rate = models.FloatField()
    created_at = models.DateTimeField()
    customer_email = models.EmailField()
    customer_firstname = models.CharField(max_length=50)
    customer_lastname = models.CharField(max_length=50)
    customer_gender = models.IntegerField()
    customer_group_id = models.BigIntegerField()
    customer_is_guest = models.IntegerField()
    customer_note_notify = models.FloatField()
    discount_amount = models.FloatField()
    email_sent = models.IntegerField()
    global_currency_code = models.CharField(max_length=10)
    grand_total = models.FloatField()
    discount_tax_compensation_amount = models.FloatField()
    increment_id = models.CharField(max_length=10)
    is_virtual = models.IntegerField()
    order_currency_code = models.CharField(max_length=10)
    protect_code = models.CharField(max_length=255)
    quote_id = models.BigIntegerField()
    remote_ip = models.CharField(max_length=50)
    shipping_amount = models.FloatField()
    shipping_description = models.CharField(max_length=150)
    shipping_discount_amount = models.FloatField()
    shipping_discount_tax_compensation_amount = models.FloatField()
    shipping_incl_tax = models.FloatField()
    shipping_tax_amount = models.FloatField()
    state = models.CharField(max_length=150)
    status = models.TextField()
    store_currency_code = models.CharField(max_length=150)
    store_id = models.BigIntegerField()
    store_name = models.TextField()
    store_to_base_rate = models.FloatField()
    store_to_order_rate = models.FloatField()
    subtotal = models.FloatField()
    subtotal_incl_tax = models.FloatField()
    tax_amount = models.FloatField()
    total_due = models.FloatField()
    total_item_count = models.IntegerField()
    total_qty_ordered = models.IntegerField()
    updated_at = models.DateTimeField()
    weight = models.FloatField()
    x_forwarded_for = models.TextField()

    class Meta:
        db_table = 'order_details'