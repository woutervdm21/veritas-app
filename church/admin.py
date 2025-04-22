from django.contrib import admin
from .models import Church, Sermon, Event  # Import models

# Registering Church model to be accessible in the admin panel
admin.site.register(Church)

# Registering Sermon and Event models
admin.site.register(Sermon)
admin.site.register(Event)