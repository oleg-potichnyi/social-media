from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from social_media.models import UserProfile
from social_media.permissions import IsAdminOrIfAuthenticatedReadOnly
from social_media.serializers import UserSerializer, UserProfileSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserProfileViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["username", "email"]

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        return queryset


class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid token or token not provided."}, status=status.HTTP_400_BAD_REQUEST)
