from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from users.models import User
from auth.serializers import UserRegisterSerializer

class CreateOnlyModeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    The viewset automatically provides 'create()' actions.
    """
    pass

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'login': reverse('token_obtain_pair', request=request, format=format),
        'refresh': reverse('token_refresh', request=request, format=format),
        'register': reverse('register-list', request=request, format=format),
    })

class RegistrationView(CreateOnlyModeViewSet):
    """View for user registration. Supports POST requests only."""

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

