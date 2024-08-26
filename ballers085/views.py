from django.shortcuts import render
from .models import Exercicios, Treinos

def index(request):
    return render(request, 'pages/index.html')
 
def treinos_categoria(request, categoria):
    try:
        treinos = Treinos.objects.filter(categoria=categoria)
        if categoria =="academia":
            return render(request, 'pages/treinos_academia.html', {'treinos': treinos, 'categoria': categoria})  
        return render(request, 'pages/treinos.html',{'treinos': treinos, 'categoria': categoria})
    except Treinos.DoesNotExist:
        return render(request,"404.html")

def psicobaska(request):
    return render(request, 'pages/psicobaska.html', {'extracss':'css/psicobaska.css'})

def treino_exercicio(request,categoria,nome_treino):
    treino_escolhido = Treinos.objects.filter(caminho_treino_url=nome_treino).first()
    try:
        exercicios = Exercicios.objects.filter(treino=treino_escolhido)
    except Exercicios.DoesNotExist:
        return render(request,"404.html")
    return render(request, 'pages/exercicios.html', {'exercicios': exercicios,"nome_treino":treino_escolhido.nome})


