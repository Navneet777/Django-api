from rest_framework import serializers
from .models import Product_Model



class Product_ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Model
        fields = '__all__'
