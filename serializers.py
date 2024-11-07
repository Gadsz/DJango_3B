# Serializers eu preciso criar junto com as urls.py dentro do nome do projeto em que estou criando
# Neste caso, "spotify" (clicar na pasta em si e posteriormente em cima em novo arquivo para evitar
# que seja criado no lugar errado).

from rest_framework import serializers
from .models import Artista, Album

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__' # Generico sem campos, somente o nome do álbum.