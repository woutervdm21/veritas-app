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
    church = models.ForeignKey(Church, on_delete=models.CASCADE, verbose_name='church') #Delete sermons if church is deleted.
    title = models.CharField(max_length=200, verbose_name='title')
    pastor = models.CharField(max_length=100, verbose_name='pastor')
    date = models.DateField(verbose_name='date')
    audio_link = models.URLField(blank=True, null=True, verbose_name='audio link')
    notes = models.TextField(blank=True, verbose_name='notes')

    def __str__(self):
        return f"{self.title} - {self.pastor}"
    
# Event Model
class Event(models.Model):
    church = models.ForeignKey(Church, on_delete=models.CASCADE, verbose_name='church') #Delete events if church is deleted.
    heading = models.CharField(max_length=100, verbose_name='heading')
    description = models.TextField(verbose_name='description')  # Better than CharField for longer text
    location = models.CharField(max_length=100, verbose_name='location')
    start_date = models.DateTimeField(verbose_name='start date')
    end_date = models.DateTimeField(verbose_name='end date')

    def __str__(self):
        return f"{self.heading} at {self.location} on {self.start_date.strftime('%Y-%m-%d %H:%M')}"
