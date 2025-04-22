from rest_framework import serializers
from .models import Church, Sermon, Event
from django.contrib.auth.models import User #Default Django User

#What is a Serializer?
#A Serializer is like a translator between:
#Python/Django objects (like a Sermon or Church model) and JSON (what APIs use)

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User #Serializing the built-in Django User model - no need to create model
        fields = ['username', 'email', 'password'] #The fields we want to include in the API
        extra_kwargs = {'password': {'write_only': True}} # Password is 'write-only' for security

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)  # Creates the user with the validated data
            return user