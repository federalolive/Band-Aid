from django.db import models
from django.urls import reverse
class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    dateformed = models.CharField(max_length=4)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"band_id": self.id})
    