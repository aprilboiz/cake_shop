from rest_framework import viewsets
from users.serializers import UserSerializer
from django.contrib.auth.models import User
from users.permissions import IsOwnerOrSuperuserOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrSuperuserOrReadOnly]