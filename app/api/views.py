from rest_framework import generics

from rest_framework.views import APIView

from app.models import *
from app.api.serializers import *

from rest_framework import viewsets
from rest_framework import permissions


class userviewset(viewsets.ModelViewSet):
    # permissions = [IsAccountAdmin]
    queryset = CustomUser.objects.filter(is_superuser=False)
    serializer_class = userAdminSerializers
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.filter(id=user.id)
        return CustomUser.objects.filter(id=user.id)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return userAdminSerializers

        return normalUserSeralizer


class activityviewset(viewsets.ModelViewSet):
    queryset = activity.objects.all()
    serializer_class = normalActivitySerializers
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            activity.objects.all()
        return activity.objects.filter(user_id=user.id)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminActivitySerializer

        return normalActivitySerializers
