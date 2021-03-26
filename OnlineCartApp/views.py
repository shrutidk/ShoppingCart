from django.shortcuts import render
from django.views.generic import ListView
from .models import Products
from OnlineCartApp.serializers import ProductSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics,permissions
from django.contrib.auth.models import User


# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAuthenticated]

    #def perform_create(self, serializer):
        #serializer.save(owner=self.request.user)


class ProdDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAuthenticated]

