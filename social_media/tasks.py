from datetime import datetime

from social_media.models import Post

from celery import shared_task


@shared_task
def schedule_post_creation(user_profile_id, content, scheduled_time):
    now = datetime.now()
    delay = scheduled_time - now
    if delay.total_seconds() <= 0:
        post = Post(user=user_profile_id, content=content)
        post.save()
    else:
        schedule_post_creation.apply_async(
            kwargs={
                "user_profile_id": user_profile_id,
                "content": content,
                "scheduled_time": scheduled_time,
            },
            countdown=delay.total_seconds(),
        )
