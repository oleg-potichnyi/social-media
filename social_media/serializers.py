from rest_framework import serializers

from social_media.models import UserProfile, Post, UserRelationship


class UserProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = "__all__"

    def get_followers_count(self, obj):
        return obj.user.followers.count()

    def get_following_count(self, obj):
        return obj.user.following.count()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class UserRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRelationship
        fields = "__all__"
