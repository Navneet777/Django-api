from rest_framework import serializers
from .models import Employee_Model



class  Employee_ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Employee_Model
        fields = '__all__'
