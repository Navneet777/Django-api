from django.shortcuts import render
from .models import Product_Model
from .serializers import Product_ModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.


@api_view(['GET', 'POST'])
def product_list(request):
    """
    List all product, or create a new product.
    """
    if request.method == 'GET':
        product = Product_Model.objects.all()
        serializer = Product_ModelSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Product_ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update or delete Product.
    """
    try:
        product = Product_Model.objects.get(pk=pk)
    except Product_Model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Product_ModelSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Product_ModelSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
