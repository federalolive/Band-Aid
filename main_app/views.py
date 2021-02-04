from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Band
from .forms import AlbumForm
from django.contrib.auth.mixins import LoginRequiredMixin

class BandCreate(LoginRequiredMixin, CreateView):
    model = Band
    fields = ['name', 'genre', 'dateformed', 'description']
    success_url = '/bands/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BandUpdate(LoginRequiredMixin, UpdateView):
    model = Band
    fields = ['genre', 'description']
class BandDelete(LoginRequiredMixin, DeleteView):
    model = Band
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
    album_form = AlbumForm()
    return render(request, 'bands/detail.html', { 
        'band': band, 'album_form': album_form 
        })

def add_album(request, band_id):
    form = AlbumForm(request.POST)
    if form.is_valid():
        new_album = form.save(commit=False)
        new_album.band_id = band_id
        new_album.save()
    return redirect('detail', band_id=band_id)