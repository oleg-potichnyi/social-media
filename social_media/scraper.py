from celery import Celery
from datetime import datetime, timedelta
from tasks import schedule_post_creation

app = Celery("app")


def schedule_post(user_profile_id, content, minutes_from_now):
    scheduled_time = datetime.now() + timedelta(minutes=minutes_from_now)
    schedule_post_creation.apply_async(args=[user_profile_id, content, scheduled_time])
