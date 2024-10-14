from rest_framework.routers import DefaultRouter
from cakes.views import CakeViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"", CakeViewSet, basename="cake")

urlpatterns = [
    path("", include(router.urls)),
]
