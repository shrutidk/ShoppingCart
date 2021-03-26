from django.shortcuts import render
from django.views.generic import ListView
from .models import Products
from OnlineCartApp.serializers import ProductSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ProductList(APIView):
    model=Products
    def get(self, request, format=None):
        prods=Products.objects.all()
        serializer = ProductSerializer(prods, many=True)
        return Response(serializer.data)
        #return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #return JsonResponse(serializer.errors, status=400)

class ProdDetails(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProductSerializer(prod)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProductSerializer(prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        prod = self.get_object(pk)
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
