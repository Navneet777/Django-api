from rest_framework import serializers
from .models import Game_store_Model



class Game_store_ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_store_Model
        fields = '__all__'
