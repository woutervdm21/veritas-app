from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Church, Sermon, Event
from .serializers import ChurchSerializer, SermonSerializer, EventSerializer, UserSerializer

# Create your views here.
#A ViewSet is where your logic goes for each endpoint (GET, POST, etc.).
#DRF gives us ModelViewSet which includes default CRUD logic already:
#ViewSets + Routers (urls.py) = Automatic endpoints with zero repetition

class ChurchViewSet(viewsets.ModelViewSet):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer

class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer 