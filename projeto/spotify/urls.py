from django.urls import path
from .views import ArtistaListCreateView

urlpatterns = [
    path('artistas/', ArtistaListCreateView.as_view(), name='artista-list-create'),
]
