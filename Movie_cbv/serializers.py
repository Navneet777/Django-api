from rest_framework import serializers
from .models import Movie_Model



class Movie_ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_Model
        fields = '__all__'
