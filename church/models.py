from django.db import models

# Create your models here.
class Sermon(models.Model):
    title = models.CharField(max_length=200)
    pastor = models.CharField(max_length=100)
    date = models.DateField()
    audio_link = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.speaker}"