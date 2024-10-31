from django.db import models

# Nesta aba será inserido as entidades do projeto, cada entidade é uma classe que
# separa as partes do projeto, neste exemplo está sendo usado 2 classes sendo elas
# "Artista" e "Album"

from django.db import models

# Inicio do Artista
# (TUDO ISSO VAI NO JSON QUANDO EXECUTADO VIA INSONMIA)

class Artista(models.Model):
    nome = models.CharField(max_length=255) # Nome dele obrigatório
    genero = models.CharField(max_length=100) # Genero da musica obrigatório
    bio = models.TextField(blank=True) # Biografia opcional

    def __str__(self):
        return self.nome

# Inicio do Album
# (TUDO ISSO VAI NO JSON QUANDO EXECUTADO VIA INSONMIA)

class Album(models.Model):
    titulo = models.CharField(max_length=255) # Titulo album obrigatório
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE) #Artista com chave estrangeira para não repetir
    data_lancamento = models.DateField() # Data de lançamento do album
    numero_de_faixas = models.IntegerField() # Número de músicas no álbum
    capa = models.URLField(blank=True)  # URL da capa do álbum

    def __str__(self):
        return self.titulo

# É possível adicionar mais classes conforme a complexidade do projeto,
# para facilitar o entendimento, neste momento será feito apenas 2 classes.
