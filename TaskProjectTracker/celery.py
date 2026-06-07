import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaskProjectTracker.settings')

app = Celery('TaskProjectTracker')

app.config_from_object('TaskProjectTracker.settings',namespace='CELERY')
app.autodiscover_tasks()
