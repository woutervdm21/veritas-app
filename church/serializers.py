from rest_framework import serializers
from .models import Church, Sermon, Event

class ChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Church
        fields = '__all__'

class SermonSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Sermon
        fields = '__all__' 

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
