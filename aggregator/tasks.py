from time import sleep

import requests
from celery import shared_task

from aggregator.models import OrderDetail, OrderBillingAddress, OrderPayment, OrderItem, OrderStatusHistory

url = "http://ec2-18-217-116-137.us-east-2.compute.amazonaws.com/rest/default/V1/orders?searchCriteria=[" \
      "currentPage]=1&searchCriteria=[pageSize]=25"
headers = {
    'Authorization': 'Bearer 6hby2nljxjoc6xe5a03240kkih2g9inv',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json'
}


def get_data():
    request = requests.get(url=url, headers=headers)
    return request.json()


@shared_task
def create_order_list():
    response = get_data()
    for item in response['items']:
        items = item.pop('items')
        billing_address = item.pop('billing_address')
        payment = item.pop('payment')
        status_histories = item.pop('status_histories')
        extension_attributes = item.pop('extension_attributes')
        order_detail = OrderDetail.objects.create(**item)
        for it in items:
            order_items = OrderItem.objects.create(**it)
        order_bill_address = OrderBillingAddress.objects.create(**billing_address)
        order_payment = OrderPayment.objects.create(**payment)
        for st in status_histories:
            order_status_histories = OrderStatusHistory.objects.create(**st)
    sleep(5)


create_order_list()
