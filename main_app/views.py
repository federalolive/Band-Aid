from django.shortcuts import render
from django.http import HttpResponse

class Band:
    def __init__(self, name, genre, description):
        self.name = name
        self.genre = genre
        self.description = description

bands = [
    Band('MCS', 'Alt', 'Awesome!')
]

def bands_index(request):
    return render(request, 'bands/index.html', { 'bands': bands })

def home(request):
    return HttpResponse('<h1>Hello</h1>')
    
def about(request):
    return render(request, 'about.html')

