from django.shortcuts import render
from rest_framework import viewsets
from .models import Church, Sermon, Event
from .serializers import ChurchSerializer, SermonSerializer, EventSerializer

# Create your views here.
class ChurchViewSet(viewsets.ModelViewSet):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer

class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer