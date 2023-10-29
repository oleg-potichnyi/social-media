import os
from datetime import timedelta

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery("app")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'schedule_post_task': {
        'task': 'social_media.tasks.schedule_post_creation',
        'schedule': timedelta(seconds=60),
    },
}

app.autodiscover_tasks(["social_media"])


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
