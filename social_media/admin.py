from django.contrib import admin

from .models import UserProfile, Post, UserRelationship

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(UserRelationship)
