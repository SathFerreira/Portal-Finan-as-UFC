from django.contrib import admin
from .models import Disciplina, TermoFinanceiro, BolsaUFC, LinkEssencial, MaterialApoio

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    # Campos que aparecerão na lista principal do Admin
    list_display = ('nome', 'semestre', 'professores', 'dificuldade')
    
    # Filtros laterais para facilitar a busca 
    list_filter = ('semestre', 'dificuldade')
    
    # Campo de busca por nome da matéria ou professor
    search_fields = ('nome', 'professores')

# Registrando os outros modelos de forma simples
admin.site.register(TermoFinanceiro)
admin.site.register(BolsaUFC) 

@admin.register(LinkEssencial)
class LinkEssencialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'url')

@admin.register(MaterialApoio)
class MaterialApoioAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('titulo', 'descricao')