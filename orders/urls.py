from django.urls import path, include

from rest_framework.routers import DefaultRouter
from orders import views

router = DefaultRouter()
router.register(r"", views.OrderViewSet, basename="order")
router.register(r"detail", views.OrderDetailViewSet, basename="order-detail")

urlpatterns = [
    path("", include(router.urls)),
]
