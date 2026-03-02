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
# --- ROTA SECRETA PARA POPULAR O BANCO DE DADOS ---
def popular_banco_secreto(request):
    try:
        # 1. LINKS ESSENCIAIS
        # Removemos para garantir que os ícones e descrições fiquem atualizados
        LinkEssencial.objects.all().delete()
        links = [
            {"nome": "SIGAA", "descricao": "Coração da vida acadêmica. Matrículas e histórico.", "url": "https://si3.ufc.br/sigaa/", "icone": "fas fa-graduation-cap"},
            {"nome": "Portal da PRAE", "descricao": "Editais de bolsas e auxílios para estudantes.", "url": "https://prae.ufc.br/", "icone": "fas fa-hand-holding-heart"},
            {"nome": "Restaurante Universitário (RU)", "descricao": "Cardápios, horários e recarga do RU.", "url": "https://www.ufc.br/restaurante/", "icone": "fas fa-utensils"},
        ]
        for item in links:
            LinkEssencial.objects.create(**item)

        # 2. BOLSAS
        bolsas = [
            {"titulo": "Bolsa de Iniciação Acadêmica (BIA 2026)", "orgao_emissor": "PRAE (Pró-Reitoria de Assistência Estudantil)", "tipo": "Auxílio Estudantil", "link_edital": "https://prae.ufc.br/pt/edital-no-01-2026-prae-ufc-bolsa-de-iniciacao-academica/", "descricao": "Destinada a estudantes de graduação presencial em situação de vulnerabilidade socioeconômica comprovada pela PRAE. Exige dedicação de 12 horas semanais em projetos acadêmicos e não permite acúmulo com outras bolsas ou emprego formal. Benefício de R$ 700,00 mensais com vigência até 31 de dezembro de 2026."},
            {"titulo": "Programa de Iniciação à Docência (PID 2026)", "orgao_emissor": "PROGRAD (Pró-Reitoria de Graduação)", "tipo": "Monitoria", "link_edital": "https://prograd.ufc.br/pt/edital-pid-no-19-2025-distribuicao-das-vagas-e-pontuacao-da-selecao-de-projetos-de-monitoria-de-iniciacao-a-docencia-em-2026/", "descricao": "Voltada para alunos de graduação que desejam atuar como monitores, auxiliando professores no processo de ensino-aprendizagem das disciplinas. Há disponibilidade de vagas remuneradas (bolsa mensal) e voluntárias, dependendo da classificação no processo seletivo do departamento."},
            {"titulo": "Programa de Bolsas de Extensão Universitária 2026", "orgao_emissor": "PREX (Pró-Reitoria de Extensão)", "tipo": "Extensão", "link_edital": "https://prex.ufc.br/pt/prex-lanca-edital-do-programa-de-bolsas-de-extensao-universitaria-2026/", "descricao": "Destinada a estudantes que atuarão em projetos e programas de extensão previamente aprovados e cadastrados na PREX, promovendo a interação entre a universidade e a sociedade. Carga horária de 12 horas semanais. Benefício de R$ 700,00 mensais (vigência de abril a dezembro de 2026)."},
            {"titulo": "Programa Institucional de Bolsas de Iniciação Científica (PIBIC 2025/2026)", "orgao_emissor": "PRPPG (Pró-Reitoria de Pesquisa e Pós-Graduação)", "tipo": "Iniciação Científica", "link_edital": "https://prppg.ufc.br/pt/prppg-editais-pibic/", "descricao": "Focada em despertar a vocação científica e incentivar talentos potenciais entre estudantes de graduação. O aluno atua em um projeto de pesquisa sob a orientação de um professor qualificado. Benefício de R$ 700,00 mensais financiadas por CNPq, FUNCAP ou pela própria UFC."},
            {"titulo": "Programa Bolsa de Incentivo ao Desporto 2026", "orgao_emissor": "SESP-UFC (Secretaria de Esportes) / PRAE", "tipo": "Auxílio Estudantil", "link_edital": "https://desporto.ufc.br/pt/com-100-vagas-secretaria-de-esportes-da-ufc-sesp-ufc-e-pro-reitoria-de-assistencia-estudantil-prae-lancam-edital-para-o-programa-bolsa-de-incentivo-ao-desporto-2026/", "descricao": "Voltada para o fomento e apoio à prática esportiva universitária. Ofertará 100 vagas para estudantes participarem de atividades desportivas representando a universidade. Vigência de 10 meses (de março a dezembro de 2026)."},
            {"titulo": "Auxílio Moradia", "orgao_emissor": "PRAE (Pró-Reitoria de Assistência Estudantil)", "tipo": "Auxílio Estudantil", "link_edital": "https://prae.ufc.br/pt/auxilio-moradia/", "descricao": "Destinado a estudantes de graduação presencial em situação de vulnerabilidade socioeconômica, cujas famílias residam em municípios diferentes da sede do campus onde estudam. O benefício é uma ajuda de custo mensal para despesas com aluguel e moradia."},
            {"titulo": "Auxílio Creche", "orgao_emissor": "PRAE (Pró-Reitoria de Assistência Estudantil)", "tipo": "Auxílio Estudantil", "link_edital": "https://prae.ufc.br/pt/auxilio-creche/", "descricao": "Voltado para estudantes (mães ou pais) de graduação presencial em situação de vulnerabilidade, que possuam filhos sob sua guarda com idade entre 6 meses e 3 anos e 11 meses. Suporte financeiro mensal."},
            {"titulo": "Isenção da Taxa do Restaurante Universitário (RU)", "orgao_emissor": "PRAE (Pró-Reitoria de Assistência Estudantil)", "tipo": "Auxílio Estudantil", "link_edital": "https://prae.ufc.br/pt/restaurante-universitario-ru/", "descricao": "Garante aos estudantes classificados socioeconomicamente o direito de realizar as refeições (almoço e jantar) de forma totalmente gratuita nos refeitórios da UFC. Essencial para a permanência estudantil."},
            {"titulo": "PIBITI (Iniciação em Desenvolvimento Tecnológico)", "orgao_emissor": "PRPPG / UFC Inova", "tipo": "Inovação", "link_edital": "https://prppg.ufc.br/pt/editais-pibiti/", "descricao": "Focado em estudantes de graduação que atuam em projetos de pesquisa aplicada, desenvolvimento tecnológico e inovação. Exige dedicação ao projeto e não possuir vínculo empregatício. Benefício mensal padrão de R$ 700,00."},
            {"titulo": "Programa de Promoção da Cultura Artística (Bolsa Arte)", "orgao_emissor": "SECULT (Secretaria de Cultura da UFC)", "tipo": "Cultura/Extensão", "link_edital": "https://secult.ufc.br/pt/bolsa-arte/", "descricao": "Destinada a alunos que desenvolvem projetos artísticos e culturais aprovados pela SECULT. Carga horária de 12 horas semanais, promovendo a arte dentro e fora dos campi. Benefício de R$ 700,00 mensais."},
            {"titulo": "BIA-PCD (Estudantes com Deficiência)", "orgao_emissor": "Secretaria de Acessibilidade / PRAE", "tipo": "Inclusão", "link_edital": "https://acessibilidade.ufc.br/", "descricao": "Bolsa de iniciação acadêmica com edital específico para estudantes com deficiência (PCD), visando a inclusão, permanência e o incentivo à vivência universitária. R$ 700,00 mensais."}
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
            {"nome": "Introdução à Economia", "semestre": 1, "dificuldade": 3, "descricao": "Esta disciplina estabelece os alicerces das duas grandes divisões do pensamento econômico, explorando como as decisões individuais e globais moldam o cenário financeiro atual. O conteúdo abrange desde a Microeconomia, com o estudo da teoria do consumidor, curvas de oferta e demanda, equilíbrios e estruturas de mercado (Monopólio, Oligopólio e Concorrência Perfeita), até a Macroeconomia, focando nos grandes agregados como PIB e PNB, índices de inflação (IPCA, IGP-M), dinâmica do desemprego e o impacto das políticas fiscais e monetárias do Banco Central. Além disso, o aluno terá uma imersão nas principais escolas que fundamentam a ciência econômica, como a Clássica, Keynesiana e Monetarista."},
            {"nome": "Matemática para Finanças I", "semestre": 1, "dificuldade": 5, "descricao": "Foco em Cálculo Diferencial. Limites, continuidade e derivadas aplicadas a problemas de otimização de funções de uma variável, visando maximização de lucros e minimização de custos."},
            {"nome": "Introdução à Contabilidade", "semestre": 1, "dificuldade": 4, "descricao": "Apresenta o método das partidas dobradas, registro de atos e fatos administrativos, e a elaboração das demonstrações financeiras fundamentais como Balanço Patrimonial e DRE."},
            {"nome": "Metodologia do Trabalho Científico", "semestre": 1, "dificuldade": 2, "descricao": "Orientação para produção acadêmica seguindo normas ABNT. Focada em pesquisa, redação de artigos e estruturação de projetos científicos de graduação."},
            {"nome": "Matemática Financeira", "semestre": 2, "dificuldade": 4, "descricao": "Regimes de capitalização simples e composta, fluxos de caixa, sistemas de amortização (SAC e Price), e análise de investimentos através de VPL e TIR."},
            {"nome": "Matemática para Finanças II", "semestre": 2, "dificuldade": 5, "descricao": "Cálculo Integral e cálculo de várias variáveis. Derivadas parciais e multiplicadores de Lagrange aplicados à otimização econômica multivariada."},
            {"nome": "Estatística para Finanças I", "semestre": 2, "dificuldade": 4, "descricao": "Probabilidades, variáveis aleatórias e distribuições. Essencial para análise de riscos e modelos econométricos futuros."},
            {"nome": "Economia Brasileira para Finanças", "semestre": 2, "dificuldade": 3, "descricao": "Histórico econômico do Brasil, analisando desde o período agroexportador até os planos de estabilização modernos (Plano Real) e crises recentes."},
            {"nome": "Contabilidade Social", "semestre": 3, "dificuldade": 4, "descricao": "Estudo das Contas Nacionais, mensurando o Produto Interno Bruto (PIB), Renda Nacional Bruta (RNB) e balanço de pagamentos."},
            {"nome": "Microeconomia I", "semestre": 3, "dificuldade": 5, "descricao": "Teoria do consumidor, teoria da firma e estruturas de mercado (concorrência perfeita e monopólio)."},
            {"nome": "Finanças Públicas", "semestre": 4, "dificuldade": 4, "descricao": "Estudo do papel do governo na economia, orçamento público, política fiscal, tributação e gastos governamentais."},
            {"nome": "Gestão de Riscos e Investimentos", "semestre": 5, "dificuldade": 5, "descricao": "Teoria de carteiras, modelo CAPM, análise de volatilidade e diversificação de ativos financeiros."},
            {"nome": "Finanças Corporativas I", "semestre": 6, "dificuldade": 5, "descricao": "Análise de estrutura de capital, custo de capital (WACC) e política de dividendos das empresas."},
            {"nome": "Avaliação de Empresas (Valuation)", "semestre": 7, "dificuldade": 5, "descricao": "Métodos de avaliação de negócios por Fluxo de Caixa Descontado (FCD) e avaliação por múltiplos de mercado."},
            {"nome": "Finanças Internacionais", "semestre": 8, "dificuldade": 4, "descricao": "Mercados de câmbio, balanço de pagamentos, e paridade do poder de compra em um cenário globalizado."}
        ]
        for item in disciplinas:
            Disciplina.objects.get_or_create(
                nome=item['nome'], 
                defaults={
                    'semestre': item['semestre'], 
                    'dificuldade': item['dificuldade'], 
                    'descricao': item['descricao']
                }
            )

        return HttpResponse("<h1 style='color: green;'>SUCESSO ABSOLUTO! BANCO POPULADO!</h1>")

    except Exception as e:
        return HttpResponse(f"<h1 style='color: red;'>ERRO:</h1><h2>{e}</h2>")