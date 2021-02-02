from django.db import models

class Band(models.Model):
    def __init__(self, name, genre, description):
        self.name = name
        self.genre = genre
        self.description = description

bands = [
    Band('MCS', 'Alt', 'Awesome!')
]