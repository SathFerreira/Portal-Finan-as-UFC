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
        # 1. LINKS ESSENCIAIS
        links = [
            {"nome": "SIGAA", "descricao": "Coração da vida acadêmica. Matrículas, notas e histórico.", "url": "https://si3.ufc.br/sigaa/", "icone": "fas fa-graduation-cap"},
            {"nome": "Portal do Estudante", "descricao": "Consulta rápida de dados e declarações de matrícula.", "url": "https://portaldodiscente.ufc.br/", "icone": "fas fa-user-graduate"},
            {"nome": "Solar (AVA)", "descricao": "Plataforma para cursos semi-presenciais e materiais de aula.", "url": "https://www.solar.ufc.br/", "icone": "fas fa-sun"},
            {"nome": "Biblioteca Universitária", "descricao": "Catálogo Pergamum para reserva de livros.", "url": "https://biblioteca.ufc.br/", "icone": "fas fa-book"},
            {"nome": "Intranet UFC", "descricao": "Acesso ao e-mail institucional (@aluno.ufc.br).", "url": "https://intranet.ufc.br/", "icone": "fas fa-envelope-open-text"},
            {"nome": "Portal da PRAE", "descricao": "Editais de bolsas e auxílios para estudantes.", "url": "https://prae.ufc.br/", "icone": "fas fa-hand-holding-heart"},
            {"nome": "Restaurante Universitário (RU)", "descricao": "Cardápios, horários e recarga de créditos do RU.", "url": "https://www.ufc.br/restaurante/", "icone": "fas fa-utensils"},
        ]
        for item in links:
            LinkEssencial.objects.get_or_create(nome=item['nome'], defaults={'descricao': item['descricao'], 'url': item['url'], 'icone': item['icone']})

        # 2. BOLSAS (USANDO BolsaUFC)
        bolsas = [
            {"nome": "Bolsa de Iniciação Acadêmica (BIA 2026)", "valor": "R$ 700,00", "descricao": "Órgão: PRAE | Tipo: Auxílio estudantil.\nDestinada a estudantes de graduação presencial em situação de vulnerabilidade socioeconômica. Exige dedicação de 12 horas semanais. Não permite acúmulo.\nLink: https://prae.ufc.br/pt/edital-no-01-2026-prae-ufc-bolsa-de-iniciacao-academica/"},
            {"nome": "Programa de Iniciação à Docência (PID 2026)", "valor": "Variável", "descricao": "Órgão: PROGRAD | Tipo: Monitoria.\nVoltada para alunos que desejam atuar como monitores auxiliando professores. Vagas remuneradas e voluntárias.\nLink: https://prograd.ufc.br/pt/edital-pid-no-19-2025-distribuicao-das-vagas-e-pontuacao-da-selecao-de-projetos-de-monitoria-de-iniciacao-a-docencia-em-2026/"},
            {"nome": "Programa de Bolsas de Extensão Universitária 2026", "valor": "R$ 700,00", "descricao": "Órgão: PREX | Tipo: Extensão.\nAtuação em projetos que promovem a interação entre a universidade e a sociedade. Carga horária de 12h semanais.\nLink: https://prex.ufc.br/pt/prex-lanca-edital-do-programa-de-bolsas-de-extensao-universitaria-2026/"},
            {"nome": "Programa Institucional de Bolsas de Iniciação Científica (PIBIC 2025/2026)", "valor": "R$ 700,00", "descricao": "Órgão: PRPPG | Tipo: Iniciação científica.\nDesperta a vocação científica atuando em projeto de pesquisa sob orientação de um professor.\nLink: https://prppg.ufc.br/pt/prppg-editais-pibic/"},
            {"nome": "Programa Bolsa de Incentivo ao Desporto 2026", "valor": "Bolsa Atleta", "descricao": "Órgão: SESP-UFC / PRAE | Tipo: Auxílio estudantil.\nFomento à prática esportiva universitária. 100 vagas para representar a universidade em atividades desportivas.\nLink: https://desporto.ufc.br/pt/com-100-vagas-secretaria-de-esportes-da-ufc-sesp-ufc-e-pro-reitoria-de-assistencia-estudantil-prae-lancam-edital-para-o-programa-bolsa-de-incentivo-ao-desporto-2026/"},
            {"nome": "Auxílio Moradia", "valor": "Ajuda de Custo", "descricao": "Órgão: PRAE | Tipo: Auxílio estudantil.\nDestinado a estudantes vulneráveis com famílias em municípios diferentes da sede do campus.\nLink: https://prae.ufc.br/pt/auxilio-moradia/"},
            {"nome": "Auxílio Creche", "valor": "Ajuda de Custo", "descricao": "Órgão: PRAE | Tipo: Auxílio estudantil.\nPara estudantes (mães/pais) vulneráveis com filhos de 6 meses a 3 anos e 11 meses.\nLink: https://prae.ufc.br/pt/auxilio-creche/"},
            {"nome": "Isenção da Taxa do Restaurante Universitário (RU)", "valor": "Isenção Total", "descricao": "Órgão: PRAE | Tipo: Auxílio estudantil.\nDireito de realizar as refeições (almoço e jantar) de forma totalmente gratuita nos refeitórios da UFC.\nLink: https://prae.ufc.br/pt/restaurante-universitario-ru/"},
            {"nome": "PIBITI (Desenvolvimento Tecnológico e Inovação)", "valor": "R$ 700,00", "descricao": "Órgão: PRPPG / UFC Inova | Tipo: Iniciação científica.\nProjetos de pesquisa aplicada, desenvolvimento tecnológico e inovação.\nLink: https://prppg.ufc.br/pt/editais-pibiti/"},
            {"nome": "Programa de Promoção da Cultura Artística (Bolsa Arte)", "valor": "R$ 700,00", "descricao": "Órgão: SECULT | Tipo: Extensão.\nParticipação em projetos artísticos e culturais aprovados pela SECULT. 12h semanais.\nLink: https://secult.ufc.br/pt/bolsa-arte/"},
            {"nome": "Bolsa de Iniciação Acadêmica para Estudantes com Deficiência (BIA-PCD)", "valor": "R$ 700,00", "descricao": "Órgão: Secretaria de Acessibilidade / PRAE | Tipo: Auxílio estudantil.\nVagas específicas para estudantes PCD visando inclusão e permanência. 12h semanais.\nLink: https://acessibilidade.ufc.br/"}
        ]
        for item in bolsas:
            BolsaUFC.objects.get_or_create(nome=item['nome'], defaults={'descricao': item['descricao'], 'valor': item['valor']})

        # 3. DISCIPLINAS (TODAS!)
        disciplinas = [
            {"nome": "Introdução à Economia", "semestre": 1, "dificuldade": 3, "descricao": "Alicerces do pensamento econômico, micro e macroeconomia."},
            {"nome": "Matemática para Finanças I", "semestre": 1, "dificuldade": 5, "descricao": "Cálculo Diferencial aplicado, limites, derivadas e otimização de lucros."},
            {"nome": "Introdução à Contabilidade", "semestre": 1, "dificuldade": 4, "descricao": "Método das partidas dobradas, Balanço Patrimonial e DRE."},
            {"nome": "Metodologia do Trabalho Científico", "semestre": 1, "dificuldade": 2, "descricao": "Normas ABNT, pesquisa acadêmica e projetos científicos."},
            {"nome": "Matemática Financeira", "semestre": 2, "dificuldade": 4, "descricao": "Juros simples/compostos, SAC, Price, VPL e TIR."},
            {"nome": "Matemática para Finanças II", "semestre": 2, "dificuldade": 5, "descricao": "Integrais, derivadas parciais e otimização avançada."},
            {"nome": "Estatística para Finanças I", "semestre": 2, "dificuldade": 4, "descricao": "Estatística descritiva, probabilidades e distribuições."},
            {"nome": "Economia Brasileira para Finanças", "semestre": 2, "dificuldade": 3, "descricao": "História econômica do Brasil, Plano Real e crises."},
            {"nome": "Teoria dos Jogos", "semestre": 5, "dificuldade": 4, "descricao": "Decisões estratégicas, Equilíbrio de Nash, jogos simultâneos e sequenciais."},
            {"nome": "Gestão de Riscos e Investimentos", "semestre": 5, "dificuldade": 5, "descricao": "Teoria Moderna de Carteiras, CAPM, Beta e VaR."},
            {"nome": "Análise de Séries Temporais para Finanças", "semestre": 5, "dificuldade": 5, "descricao": "Modelos preditivos como ARIMA e modelos de volatilidade como GARCH."},
            {"nome": "Finanças Corporativas I", "semestre": 6, "dificuldade": 4, "descricao": "Estrutura de capital, WACC, política de dividendos, VPL e TIR."},
            {"nome": "Mercado de Capitais", "semestre": 6, "dificuldade": 4, "descricao": "Bolsa de Valores, ações, debêntures, IPO e papel da CVM."},
            {"nome": "Econometria para Finanças II", "semestre": 6, "dificuldade": 5, "descricao": "Modelos de dados em painel, variáveis instrumentais, heterocedasticidade."},
            {"nome": "Derivativos Financeiros", "semestre": 6, "dificuldade": 5, "descricao": "Opções, Contratos Futuros, Swaps, e modelo Black-Scholes."},
            {"nome": "Avaliação de Empresas", "semestre": 7, "dificuldade": 5, "descricao": "Valuation, Fluxo de Caixa Descontado (FCD) e avaliação por múltiplos."},
            {"nome": "Sistema Financeiro Nacional", "semestre": 7, "dificuldade": 3, "descricao": "Estrutura do SFN, CMN, Bacen, CVM e regulação bancária."},
            {"nome": "Monografia I", "semestre": 7, "dificuldade": 4, "descricao": "Definição do tema de pesquisa, problema e referencial teórico do TCC."},
            {"nome": "Finanças Internacionais", "semestre": 8, "dificuldade": 4, "descricao": "Mercado de câmbio, paridade do poder de compra e balanço de pagamentos."},
            {"nome": "Monografia II", "semestre": 8, "dificuldade": 4, "descricao": "Defesa do TCC, análise de dados e redação dos resultados."}
        ]
        for item in disciplinas:
            Disciplina.objects.get_or_create(nome=item['nome'], defaults={'semestre': item['semestre'], 'dificuldade': item['dificuldade'], 'descricao': item['descricao']})

        return HttpResponse("<h1 style='color: green;'>SUCESSO ABSOLUTO! O BANCO DE DADOS FOI ATUALIZADO COM TODAS AS BOLSAS, LINKS E DISCIPLINAS!</h1>")
    
    except Exception as e:
        return HttpResponse(f"<h1 style='color: red;'>ERRO:</h1><h2>{e}</h2>")