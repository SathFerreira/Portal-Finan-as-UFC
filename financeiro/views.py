from django.shortcuts import render
from django.http import HttpResponse
from .models import Disciplina, TermoFinanceiro, BolsaUFC, LinkEssencial, MaterialApoio
from django.db.models import Q
from django.core.paginator import Paginator

# Página inicial
def home(request):
    return render(request, 'financeiro/home.html')

# Dicionário
def dicionario(request):
    query = request.GET.get('search', '').strip()
    termos_list = TermoFinanceiro.objects.all().order_by('termo')

    if query:
    
        resultados_inicio = termos_list.filter(termo__istartswith=query)
        
       
        resultados_meio = termos_list.filter(
            Q(termo__icontains=query) | Q(definicao__icontains=query)
        ).exclude(id__in=resultados_inicio)

        termos_filtrados = list(resultados_inicio) + list(resultados_meio)
        total_count = len(termos_filtrados)
    else:
        termos_filtrados = termos_list
        total_count = termos_list.count()

    paginator = Paginator(termos_filtrados, 20)
    page_number = request.GET.get('page')
    termos_paginados = paginator.get_page(page_number)

    return render(request, 'financeiro/dicionario.html', {
        'termos': termos_paginados,
        'termo_pesquisado': query,
        'total': total_count
    })

# Outras Views (Disciplinas, Bolsas, Links e Materiais)
def lista_disciplinas(request):
    materias = Disciplina.objects.all()
    return render(request, 'financeiro/disciplinas.html', {'disciplinas': materias})

def bolsas(request):
    vagas = BolsaUFC.objects.all()
    return render(request, 'financeiro/bolsas.html', {'bolsas': vagas})

def links_essenciais(request):
    lista_links = LinkEssencial.objects.all()
    return render(request, 'financeiro/links.html', {'links': lista_links})

def materiais(request):
    return render(request, 'financeiro/materiais.html')
# --- ROTA SECRETA PARA POPULAR O BANCO DE DADOS ---
def popular_banco_secreto(request):
    try:
        # 1. LINKS ESSENCIAIS (Manteve igual, pois passou sem erros)
        links = [
            {"nome": "SIGAA", "descricao": "Coração da vida acadêmica. Matrículas e histórico.", "url": "https://si3.ufc.br/sigaa/", "icone": "fas fa-graduation-cap"},
            {"nome": "Portal da PRAE", "descricao": "Editais de bolsas e auxílios para estudantes.", "url": "https://prae.ufc.br/", "icone": "fas fa-hand-holding-heart"},
            {"nome": "Restaurante Universitário (RU)", "descricao": "Cardápios, horários e recarga do RU.", "url": "https://www.ufc.br/restaurante/", "icone": "fas fa-utensils"},
        ]
        for item in links:
            LinkEssencial.objects.get_or_create(nome=item['nome'], defaults={'descricao': item['descricao'], 'url': item['url'], 'icone': item['icone']})

        # 2. BOLSAS (CORRIGIDO COM AS COLUNAS EXATAS DO SEU BANCO!)
        bolsas = [
            {"titulo": "Bolsa de Iniciação Acadêmica (BIA 2026)", "orgao_emissor": "PRAE", "tipo": "Auxílio estudantil", "link_edital": "https://prae.ufc.br/pt/edital-no-01-2026-prae-ufc-bolsa-de-iniciacao-academica/", "descricao": "Para alunos em vulnerabilidade. R$ 700,00."},
            {"titulo": "Programa de Iniciação à Docência (PID 2026)", "orgao_emissor": "PROGRAD", "tipo": "Monitoria", "link_edital": "https://prograd.ufc.br/", "descricao": "Vagas remuneradas e voluntárias para monitores."},
            {"titulo": "Bolsas de Extensão Universitária 2026", "orgao_emissor": "PREX", "tipo": "Extensão", "link_edital": "https://prex.ufc.br/", "descricao": "Atuação em projetos de extensão. R$ 700,00."},
            {"titulo": "PIBIC 2025/2026", "orgao_emissor": "PRPPG", "tipo": "Iniciação científica", "link_edital": "https://prppg.ufc.br/pt/prppg-editais-pibic/", "descricao": "Projeto de pesquisa científica. R$ 700,00."},
            {"titulo": "Isenção do RU", "orgao_emissor": "PRAE", "tipo": "Auxílio estudantil", "link_edital": "https://prae.ufc.br/pt/restaurante-universitario-ru/", "descricao": "Refeições gratuitas nos refeitórios da UFC."}
        ]
        for item in bolsas:
            BolsaUFC.objects.get_or_create(
                titulo=item['titulo'], 
                defaults={
                    'orgao_emissor': item['orgao_emissor'], 
                    'tipo': item['tipo'], 
                    'link_edital': item['link_edital'], 
                    'descricao': item['descricao']
                }
            )

        # 3. DISCIPLINAS
        disciplinas = [
            {"nome": "Introdução à Economia", "semestre": 1, "dificuldade": 3, "descricao": "Micro e macroeconomia."},
            {"nome": "Matemática para Finanças I", "semestre": 1, "dificuldade": 5, "descricao": "Cálculo Diferencial aplicado."},
            {"nome": "Introdução à Contabilidade", "semestre": 1, "dificuldade": 4, "descricao": "Balanço Patrimonial e DRE."},
            {"nome": "Matemática Financeira", "semestre": 2, "dificuldade": 4, "descricao": "Juros simples/compostos, VPL e TIR."}
        ]
        for item in disciplinas:
            Disciplina.objects.get_or_create(nome=item['nome'], defaults={'semestre': item['semestre'], 'dificuldade': item['dificuldade'], 'descricao': item['descricao']})

        return HttpResponse("<h1 style='color: green;'>SUCESSO ABSOLUTO! BANCO POPULADO!</h1>")
    
    except Exception as e:
        return HttpResponse(f"<h1 style='color: red;'>ERRO:</h1><h2>{e}</h2>")