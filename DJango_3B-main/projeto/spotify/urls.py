from django.urls import path
from .views import ArtistaListCreateView, AlbumListCreateView, ArtistaReadUpdateDeleteView

# Ao abrir o Insomnia, ejetar o Ctrl J para abrir terminal (No VScode) e executar "python3 manage.py runserver" 

urlpatterns = [
    path('artistas/', ArtistaListCreateView.as_view(), name='artista-list-create'), # E esse é o de artista, o que muda
    #"path('NOME DA VARIÁVEL/', NOME DA VARIÁVELlistCreateView.as_view(), name='NOME DA VARIÁVEL-list-create'),"
    path('artistas/<int:pk>/', ArtistaReadUpdateDeleteView.as_view()), #UPDATE E DELETE
    path('album/', AlbumListCreateView.as_view(), name='album-list-create'), # Esse é o caminho para criar (CRUD) de álbum
]

# Nesta parte quando abrir o Insomnia o que será adicionado na url da new request será o nome do path que é o
# nome da view que irei trabalhar.

# NÃO SE ESQUECER DENTRO DO INSOMNIA DE ALTERAR O BODY PARA JSON (EMBAIXO DO POST/GET, SEGUNDO BOTÃO A DIREITA).