"""
URL configuration for Veritas_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from church.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('church.urls')),  # This includes the APIs
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
]

#Django / REST Framework terminology

#Model | A Python class that defines your DB table (Church, Sermon, etc.)
#Serializer | Translates between model objects and JSON (used in APIs)
#View / ViewSet | Logic for handling requests (GET/POST/etc.)
#Router | Auto-generates REST URLs from ViewSets
#QuerySet | A collection of model objects from the DB
#URLconf | The mapping of URLs to views (via urls.py)
#Admin Panel | Auto-generated UI to manage models (enabled via admin.py)
#Migration | Version control for your database structure
#Slug | URL-safe, unique identifier (e.g., "sermon-on-hope")
#ForeignKey | A link to another model (e.g., Sermon → Church)
#DRF | Django REST Framework, the toolkit we're using for APIs

#Frontend (React/HTML/Flutter)
#     |
#     v
#API URLs (e.g. /api/sermons/)
#     |
#     v
#Router → ViewSet → Serializer → Model → SQLite Database