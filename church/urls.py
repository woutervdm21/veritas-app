from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChurchViewSet, SermonViewSet, EventViewSet

router = DefaultRouter()
router.register(r'churches', ChurchViewSet)
router.register(r'sermons', SermonViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
