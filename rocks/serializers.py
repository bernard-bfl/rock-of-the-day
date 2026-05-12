from rest_framework import serializers
from .models import Rock

class RockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rock 
        fields = '__all__'