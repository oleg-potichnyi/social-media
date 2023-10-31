from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", null=True, blank=True
    )
    bio = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs) -> None:
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_time = models.DateTimeField(null=True, blank=True)
    is_scheduled = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]


class UserRelationship(models.Model):
    from_user = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
