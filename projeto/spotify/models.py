from django.db import models

# Nesta aba será inserido as entidades do projeto, cada entidade é uma classe que
# separa as partes do projeto, neste exemplo está sendo usado 2 classes sendo elas
# "Artista" e "Album"

from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    titulo = models.CharField(max_length=255)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    data_lancamento = models.DateField()
    numero_de_faixas = models.IntegerField()
    capa = models.URLField(blank=True)  # URL da capa do álbum

    def __str__(self):
        return self.titulo

# É possível adicionar mais classes conforme a complexidade do projeto,
# para facilitar o entendimento, neste momento será feito apenas 2 classes.