from django.shortcuts import render
from rest_framework import viewsets
from api.models import Product
from api.serializer import ProductSerializer

# Create your views here.

class ProductViews (viewsets.ModelViewSet):
    queryset = Product.objects.all()
    productSerializer_class = ProductSerializer
