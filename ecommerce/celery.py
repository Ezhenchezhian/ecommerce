import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
app = Celery('ecommerce')
app.config_from_object('ecommerce.settings', namespace='CELERY')
app.conf.beat_schedule = {
    'daily': {
        'task': 'create_order_list',
        'schedule': crontab(hour='6, 18', minute=0)
    }
}
app.autodiscover_tasks()
