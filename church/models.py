from django.db import models

class Church(models.Model):
    name = models.CharField(max_length=100) # primary_key=True if name is PK, we will use default Django ID auto-increment field
    # Django automatically creates an 'id' primary key field
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    location = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

# Sermon Model
class Sermon(models.Model):
    church = models.ForeignKey(Church, on_delete=models.CASCADE) #Delete sermons if church is deleted.
    title = models.CharField(max_length=200)
    pastor = models.CharField(max_length=100)
    date = models.DateField()
    audio_link = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.speaker}"
    
# Event Model
class Event(models.Model):
    church = models.ForeignKey(Church, on_delete=models.CASCADE) #Delete events if church is deleted.
    heading = models.CharField(max_length=100)
    description = models.TextField()  # Better than CharField for longer text
    location = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} at {self.location} on {self.start_date.strftime('%Y-%m-%d %H:%M')}"