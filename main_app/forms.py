from django.forms import ModelForm
from .models import Album

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['release_date', 'name']