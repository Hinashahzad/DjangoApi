# Serializer convert the data comming from MODEL into JSON Format

from rest_framework import routers, serializers, viewsets
from api.models import Product

class ProductSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'