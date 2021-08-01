from django.contrib.postgres.fields import ArrayField
from django.db import models


class ExtensionAttribute(models.Model):
    converting_from_quote = models.BooleanField(default=False)
    customer_data = models.JSONField()
    order_items_custom_fields = ArrayField(models.JSONField(), size=50)
