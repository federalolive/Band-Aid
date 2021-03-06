from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bands/', views.bands_index, name='index'),
    path('bands/<int:band_id>/', views.bands_detail, name='detail'),
    path('bands/create/', views.BandCreate.as_view(), name='bands_create'),
    path('bands/<int:pk>/update/', views.BandUpdate.as_view(), name='bands_update'),
    path('bands/<int:pk>/delete/', views.BandDelete.as_view(), name='bands_delete'),
    path('bands/<int:band_id>/add_album/', views.add_album, name='add_album'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('cats/<int:band_id>/assoc_similarband/<int:similarband_id>/', views.assoc_similarband, name='assoc_similarband'),
    path('cats/<int:band_id>/unassoc_similarband/<int:similarband_id>/', views.unassoc_similarband, name='unassoc_similarband'),
]