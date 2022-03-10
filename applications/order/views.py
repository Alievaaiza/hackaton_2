from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from applications.order.models import Order
from applications.order.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        return {'request': self.request}

