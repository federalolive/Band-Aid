from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class SimilarBand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bands_detail', kwargs={'pk': self.id})
class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    dateformed = models.CharField(max_length=4)
    description = models.TextField(max_length=250)
    SimilarBands = models.ManyToManyField(SimilarBand)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'band_id': self.id})
    
class Album(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField('release date')
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.get_album_display()} on {self.date}"
