from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Band

def BandCreate(CreateView):
    model = Band
    fields = '__all__'
    success_url = '/bands/'

def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def bands_index(request):
    bands = Band.objects.all()
    return render(request, 'bands/index.html', { 'bands': bands })
    
def bands_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'bands/detail.html', { 'band': band })