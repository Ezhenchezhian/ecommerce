from django.db import models
from django.contrib.postgres.fields import ArrayField

from aggregator.models.orders.order_details import OrderDetail


class OrderBillingAddress(models.Model):
    entity_id = models.BigIntegerField()
    address_type = models.TextField()
    city = models.TextField()
    company = models.TextField()
    country_id = models.CharField(max_length=10)
    customer_address_id = models.BigIntegerField()
    email = models.EmailField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    postcode = models.TextField()
    region = models.TextField()
    region_code = models.IntegerField()
    region_id = models.IntegerField()
    street = ArrayField(models.TextField(), blank=True, size=255)
    telephone = models.TextField()
    parent_id = models.ForeignKey(OrderDetail, on_delete=models.PROTECT, related_name='billing_address')

    class Meta:
        db_table = 'order_billing_addresses'
