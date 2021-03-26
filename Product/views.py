from django.shortcuts import render

from .orderpermission import CanOrder, IsAuthenticated
from .models import Orders
from Product.serializers import OrderSerializer
from rest_framework import status, generics

# Create your views here.


class OrderList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,]

class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
