from django.shortcuts import render
from .models import Exercicios, Treinos
from datetime import datetime
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'pages/index.html')
 
def treinos_categoria(request, categoria):
    try:
        treinos = Treinos.objects.filter(categoria=categoria, data_criacao__lte=datetime.now()).order_by('-data_criacao')
        if treinos.count() == 0:
            return render(request, 'pages/404.html')

        if categoria =="academia":
            return render(request, 'pages/treinos_academia.html', {'treinos': treinos, 'categoria': categoria})  
        return render(request, 'pages/treinos.html',{'treinos': treinos, 'categoria': categoria})
    except Treinos.DoesNotExist:
        return render(request,"pages/404.html")

def psicobaska(request):
    return render(request, 'pages/psicobaska.html', {'extracss':'css/psicobaska.css'})

def treino_exercicio(request, categoria, nome_treino):
    try:
        treino_escolhido = get_object_or_404(Treinos,caminho_treino_url=nome_treino)
        exercicios = Exercicios.objects.filter(treino=treino_escolhido)
        return render(request, 'pages/exercicios.html', {'exercicios': exercicios, "nome_treino": treino_escolhido.nome})
    except Exercicios.DoesNotExist:
        return render(request, "404.html")


