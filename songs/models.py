from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=20)
    artist = models.CharField(max_length=10)

    def __str__(self):
        return self.name+" -- "+self.artist