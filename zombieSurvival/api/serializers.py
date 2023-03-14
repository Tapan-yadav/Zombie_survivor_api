from rest_framework import serializers
from .models import Survivor


class SurvivorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Survivor
        fields = ('id','name', 'age', 'gender', 'longitude', 'latitude', 'is_infected','count_reports') 
        
        
class Survivor_LocationSerializer(serializers.ModelSerializer):
    """
    A survivor location serializer to return the items in inventory
    """
    class Meta:
        model = Survivor
        fields = ('longitude', 'latitude')
        