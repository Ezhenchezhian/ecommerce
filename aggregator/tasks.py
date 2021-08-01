from time import sleep
from celery.contrib import rdb

import requests
from celery import shared_task

from aggregator.models import OrderDetail

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
        OrderDetail.objects.create(**item)
    sleep(5)


@shared_task
def update_order_list():
    pass


create_order_list()
while True:
    sleep(15)
    update_order_list()
