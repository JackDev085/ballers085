from django.db import models


class Treinos(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    descricao = models.TextField(max_length=40)
    duracao = models.CharField(max_length=30)
    link_video_treino = models.CharField(max_length=50, default="RpC7sv8_LIg")
    data_criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=30, default='Treino')
    caminho_treino_url = models.CharField(max_length=30, default='nome_treino')

    def __str__(self):
        return self.nome

class Exercicios(models.Model):
    nome = models.CharField(max_length=30)
    repeticoes = models.CharField(max_length=30)
    link = models.CharField(max_length=100)
    treino = models.ForeignKey(Treinos, on_delete=models.CASCADE, related_name='exercicios')

    def __str__(self):
        return self.nome
