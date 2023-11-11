from django.urls import path, include
from rest_framework import routers

from social_media.views import (
    UserProfileViewSet,
    PostViewSet,
    UserRelationshipViewSet,
    FollowUserView,
    UnfollowUserView,
    CreatePostView,
)

app_name = "social_media"

router = routers.DefaultRouter()
router.register("user_profiles", UserProfileViewSet)
router.register("post", PostViewSet)
router.register("user_relationship", UserRelationshipViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),
    path("create_post/", CreatePostView.as_view(), name="create_post"),
]
