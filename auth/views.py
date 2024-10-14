from rest_framework import viewsets
from rest_framework import mixins
from users.models import User
from auth.serializers import UserRegisterSerializer


class RegistrationView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """View for user registration. Supports POST requests only."""

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
