from django.urls import path
from django.shortcuts import render
from django.conf.urls import handler404
from ballers085 import views
def custom_404(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('', views.index, name='index'),
    path('psicobaska/', views.psicobaska, name='psicobaska'),  # Adiciona a URL de login
    path('treinos/<str:categoria>/', views.treinos_categoria, name='treinos_categoria'),
    path('treinos/<str:categoria>/<str:nome_treino>', views.treino_exercicio, name='treino_exercicio'),
]   
handler404 = custom_404

