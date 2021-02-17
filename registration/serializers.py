from rest_framework import serializers
from .models import Registrations



class RegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrations
        fields = ['first_name','last_name','email','password','create_date']
