from rest_framework import viewsets
from cakes.models import Cake
from cakes.serializers import CakeSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CakeViewSet(viewsets.ModelViewSet):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return []
        return [IsAuthenticated(), IsAdminUser()]
