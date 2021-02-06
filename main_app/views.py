from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import boto3
import uuid
from .models import Band, SimilarBand
from .forms import AlbumForm

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid credentials - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

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

@login_required
def bands_index(request):
    bands = Band.objects.filter(user=request.user)
    return render(request, 'bands/index.html', { 'bands': bands })

@login_required    
def bands_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    similarbands_band_not_linked = SimilarBand.objects.exclude(id__in = band.similarbands.all().values_list('id'))
    album_form = AlbumForm()
    return render(request, 'bands/detail.html', { 
        'band': band, 'album_form': album_form,
        'similarbands': similarbands_band_not_linked
        })

@login_required
def add_album(request, band_id):
    form = AlbumForm(request.POST)
    if form.is_valid():
        new_album = form.save(commit=False)
        new_album.band_id = band_id
        new_album.save()
    return redirect('detail', band_id=band_id)

@login_required
def assoc_similarband(request, band_id, similarband_id):
  Band.objects.get(id=band_id).similarbands.add(band_id)
  return redirect('detail', band_id=band_id)

@login_required
def unassoc_similarband(request, band_id, similarband_id):
  Band.objects.get(id=band_id).SimilarBands.remove(similarband_id)
  return redirect('detail', band_id=band_id)