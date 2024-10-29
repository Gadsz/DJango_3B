from django.shortcuts import render

# Create your views here.

# Parte analisado da views.py do exemplo "biblioteca"
# do professor.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Artista, Album
from .serializers import ArtistaSerializer, AlbumSerializer

class ArtistaListCreateView(APIView):
    def post(self, request):
        serializer = ArtistaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        artistas = ArtistaSerializer.objects.all()
        serializer = ArtistaSerializer(artistas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AlbumListCreateView(APIView):
    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        albums = AlbumSerializer.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)