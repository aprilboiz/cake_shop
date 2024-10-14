from rest_framework import viewsets
from django.contrib.auth.models import User
from users import serializers
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnerOrSuperuserOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return []
        return [IsAuthenticated(), IsOwnerOrSuperuserOrReadOnly()]
