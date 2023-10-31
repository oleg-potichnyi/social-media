from django.shortcuts import get_object_or_404
from rest_framework import mixins, status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from social_media.models import UserProfile, Post, UserRelationship
from social_media.permissions import IsAdminOrIfAuthenticatedReadOnly
from social_media.serializers import (
    UserProfileSerializer,
    PostSerializer, UserRelationshipSerializer,
)
from user.models import User


class UserProfileViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class PostViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class UserRelationshipViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = UserRelationship.objects.all()
    serializer_class = UserRelationshipSerializer
    permission_classes = [IsAuthenticated, IsAdminOrIfAuthenticatedReadOnly]


class FollowUserView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user_to_follow_id = kwargs.get('user_id')
        user_to_follow = get_object_or_404(User, id=user_to_follow_id)

        relationship, created = UserRelationship.objects.get_or_create(
            from_user=request.user,
            to_user=user_to_follow,
        )

        if created:
            return Response(
                {"message": "You are now following this user."},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"message": "You are already following this user."},
                status=status.HTTP_200_OK
            )


class UnfollowUserView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        user_to_unfollow_id = kwargs.get('user_id')
        user_to_unfollow = get_object_or_404(User, id=user_to_unfollow_id)

        relationship = UserRelationship.objects.filter(
            from_user=request.user,
            to_user=user_to_unfollow,
        ).first()

        if relationship:
            relationship.delete()
            return Response(
                {"message": "You have unfollowed this user."},
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {"message": "You were not following this user."},
                status=status.HTTP_200_OK
            )
