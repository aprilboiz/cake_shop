from rest_framework import viewsets
from orders.models import Order, OrderDetail, OrderStatus
from orders.serializers import (
    OrderSerializer,
    OrderDetailSerializer,
    OrderStatusSerializer,
)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetailViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()


class OrderStatusViewSet(viewsets.ModelViewSet):
    serializer_class = OrderStatusSerializer
    queryset = OrderStatus.objects.all()
