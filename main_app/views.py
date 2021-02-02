from django.shortcuts import render
from .models import Band

class Band:
    def __init__(self, name, genre, dateformed, description):
        self.name = name
        self.genre = genre
        self.dateformed = dateformed
        self.description = description

bands = [
    Band('MCS', 'Alt', '1997', 'Awesome!')
]

def bands_index(request):
    bands = Band.objects.all()
    return render(request, 'bands/index.html', { 'bands': bands })

def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

