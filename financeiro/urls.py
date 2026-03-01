
from django.urls import path
from . import views

urlpatterns = [
    # Rota para a Página Inicial
    path('', views.home, name='home'),
    
    # Rota para as Disciplinas
    path('disciplinas/', views.lista_disciplinas, name='disciplinas'),
    
    # Rota para o Dicionário
    path('dicionario/', views.dicionario, name='dicionario'),
    
    # Rota para as Bolsas da UFC
    path('bolsas/', views.bolsas, name='bolsas'),

    # Rota para os Links essenciais
    path('links/', views.links_essenciais, name='links'),
    
        # Rota para os Materiais de apoio 
    path('materiais/', views.materiais, name='materiais'),
]