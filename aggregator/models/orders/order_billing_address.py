from django.db import models
from django.contrib.postgres.fields import ArrayField

from aggregator.models.orders.order_details import OrderDetail


class OrderBillingAddress(models.Model):
    entity_id = models.BigIntegerField()
    address_type = models.TextField(null=True)
    city = models.TextField(null=True)
    company = models.TextField(null=True)
    country_id = models.CharField(max_length=255,null=True)
    customer_address_id = models.BigIntegerField(null=True)
    email = models.EmailField(null=True)
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    postcode = models.TextField(null=True)
    region = models.TextField(null=True)
    region_code = models.TextField(null=True)
    region_id = models.IntegerField(null=True)
    street = ArrayField(models.TextField(null=True), blank=True, size=255, null=True)
    telephone = models.TextField(null=True)
    parent_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'order_billing_addresses'
