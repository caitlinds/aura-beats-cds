from django.db import models

class Moods(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
