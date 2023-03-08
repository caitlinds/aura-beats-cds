from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Song(models.Model):
  name = models.CharField(max_length=50)
  artist = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
        return reverse('songs_detail', kwargs={'song_id': self.id})
  
class Video(models.Model):
    title = models.CharField(max_length=500)
    thumbnail = models.URLField(max_length=500)
    video_id = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
      return f'{self.title} ({self.video_id})'

class Mood(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, related_name="favorites", blank=True)
    genmood = models.BooleanField(default=False)
    videos = models.ManyToManyField(Video, related_name="moods", blank=True)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'mood_id': self.id})    
    
class Song(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=250)
    
    mood = models.ForeignKey(
    Mood,
    on_delete=models.CASCADE
  )
    
    def __str__(self):
        return f'{self.title} ({self.url})'

class Photo(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.mood} ({self.url})'







    


