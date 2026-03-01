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
  {
    "nome": "Introdução à Economia",
    "semestre": 1,
    "dificuldade": 3,
    "descricao": "Aborda os fundamentos da teoria econômica, microeconomia (consumidor, mercados) e macroeconomia (PIB, inflação, desemprego, políticas fiscal e monetária). Inclui as escolas Clássica, Keynesiana e Monetarista."
  },
  {
    "nome": "Matemática para Finanças I",
    "semestre": 1,
    "dificuldade": 5,
    "descricao": "Foca no Cálculo Diferencial aplicado a finanças. Abrange modelagem de funções, limites, continuidade e derivadas para otimização (lucro máximo e custo mínimo) em operações financeiras e de mercado."
  },
  {
    "nome": "Introdução à Contabilidade",
    "semestre": 1,
    "dificuldade": 4,
    "descricao": "Introdução às técnicas de registro e estrutura contábil. Aborda o Método das Partidas Dobradas, Plano de Contas (Ativos, Passivos, Patrimônio Líquido) e a análise de demonstrações financeiras (Balanço Patrimonial e DRE)."
  },
  {
    "nome": "Metodologia do Trabalho Científico",
    "semestre": 1,
    "dificuldade": 2,
    "descricao": "Foco na escrita acadêmica, rigor do método científico, curadoria de fontes confiáveis, Normas ABNT (citações/referências) e estruturação de trabalhos (resumos, projetos de pesquisa)."
  },
  {
    "nome": "Matemática Financeira",
    "codigo": "FNA0005",
    "semestre": 2,
    "dificuldade": 4,
    "descricao": "Base prática sobre o valor do dinheiro no tempo e operações de mercado. Estudo de juros simples/compostos, taxas nominais/efetivas, sistemas de amortização (SAC, Price) e análise de viabilidade (VPL, TIR)."
  },
  {
    "nome": "Matemática para Finanças II",
    "codigo": "FNA0006",
    "semestre": 2,
    "dificuldade": 5,
    "descricao": "Continuação do cálculo diferencial, focando no estudo de integrais (acumulação de valores), funções de várias variáveis, derivadas parciais e otimização avançada sob múltiplas restrições financeiras."
  },
  {
    "nome": "Estatística para Finanças I",
    "codigo": "FNA0007",
    "semestre": 2,
    "dificuldade": 4,
    "descricao": "Introdução à análise de dados para previsão de riscos e retornos. Abrange estatística descritiva (média, desvio padrão), teoria das probabilidades, distribuições de frequência e estudo de correlação."
  },
  {
    "nome": "Economia Brasileira para Finanças",
    "codigo": "FNA0008",
    "semestre": 2,
    "dificuldade": 3,
    "descricao": "Análise crítica e histórica da economia brasileira. Estudo dos ciclos históricos, planos de estabilização (ênfase no Plano Real), crises econômicas, dívida pública, reformas estruturais e desafios no cenário globalizado."
  },
  {
    "nome": "Microeconomia I",
    "codigo": "FNA0010",
    "semestre": 2,
    "dificuldade": 4,
    "descricao": "Aprofunda a análise do comportamento de consumidores (curvas de indiferença) e firmas (funções de produção, custos). Foca no equilíbrio em mercados perfeitamente competitivos e exige base em álgebra aplicada a gráficos."
  },
  {
    "nome": "Macroeconomia I",
    "codigo": "FNA0011",
    "semestre": 2,
    "dificuldade": 4,
    "descricao": "Estudo da economia agregada e as forças da riqueza nacional. Foco no Modelo IS-LM (equilíbrio bens/monetário) e Oferta/Demanda Agregada. Analisa o impacto dos gastos do governo e taxas de juros no PIB nacional."
  },
  {
    "nome": "Estatística para Finanças II",
    "codigo": "FNA0012",
    "semestre": 2,
    "dificuldade": 4,
    "descricao": "Foca em Estatística Inferencial. Abrange testes de hipóteses, intervalos de confiança e distribuições (t-Student, Qui-quadrado). Introdução à regressão linear simples para previsão de variáveis financeiras."
  },
  {
    "nome": "Álgebra Linear para Finanças",
    "codigo": "FNA0013",
    "semestre": 2,
    "dificuldade": 5,
    "descricao": "Base matemática para gerenciamento de carteiras. Estudo de vetores, matrizes, sistemas de equações e transformações lineares. Inclui conceitos de autovalores/autovetores essenciais para computação e modelagem financeira."
  },
  {
    "nome": "Econometria I",
    "codigo": "FNA0015",
    "semestre": 3,
    "dificuldade": 5,
    "descricao": "Une economia, matemática e estatística para testar hipóteses com dados reais. Foca no Modelo de Regressão Linear Múltipla, incluindo identificação e correção de problemas como heterocedasticidade e autocorrelação."
  },
  {
    "nome": "Finanças Corporativas I",
    "semestre": 3,
    "dificuldade": 4,
    "descricao": "Gestão interna e decisões estratégicas de investimento e financiamento. Aborda estrutura de capital, Custo Médio Ponderado de Capital (WACC), políticas de dividendos e avaliação de projetos/empresas (retorno e risco)."
  },
  {
    "nome": "Mercado de Capitais",
    "semestre": 3,
    "dificuldade": 3,
    "descricao": "Imersão no funcionamento da Bolsa de Valores e sistemas globais. Detalha emissão/negociação de ações, debêntures, títulos públicos, derivativos/contratos futuros. Analisa o papel de corretoras, bancos de investimento e CVM."
  },
  {
    "nome": "Gestão de Riscos",
    "semestre": 3,
    "dificuldade": 4,
    "descricao": "Ensina a identificar, medir e mitigar incertezas em ativos financeiros. Aborda riscos de mercado, crédito, operacional e liquidez, usando ferramentas como o Value at Risk (VaR), instrumentos de hedge e diversificação."
  },
  {
    "nome": "Microeconomia II",
    "codigo": "FNA0015",
    "semestre": 4,
    "dificuldade": 4,
    "descricao": "Expande a microeconomia para falhas de mercado real. Foca em Teoria dos Jogos, modelos de Oligopólio (Cournot, Bertrand) e Monopólio. Analisa o impacto de externalidades e informação assimétrica."
  },
  {
    "nome": "Métodos Computacionais Aplicados às Finanças",
    "codigo": "FNA0016",
    "semestre": 4,
    "dificuldade": 4,
    "descricao": "Fusão de tecnologia e finanças, usando linguagens (Python/R). Foca na automação de cálculos, Simulações de Monte Carlo e manipulação de Big Data. Desenvolvimento de algoritmos de otimização de carteiras."
  },
  {
    "nome": "Econometria para Finanças I",
    "codigo": "FNA0017",
    "semestre": 4,
    "descricao": "Pilar analítico que une Economia, Matemática e Estatística. Foco na construção e interpretação de modelos de Regressão Linear Múltipla para entender a influência de diversas variáveis (juros, inflação, câmbio) em ativos. Inclui testes de diagnóstico avançados."
  },
  {
    "nome": "Teoria dos Jogos",
    "codigo": "FNA0020",
    "semestre": 5,
    "dificuldade": 4,
    "descricao": "Estudo das decisões estratégicas onde o resultado depende de múltiplos 'jogadores'. Explora o Equilíbrio de Nash, jogos simultâneos/sequenciais, Dilema do Prisioneiro e estratégias dominantes. Essencial para analisar negociações e concorrência."
  },
  {
    "nome": "Gestão de Riscos e Investimentos",
    "codigo": "FNA0021",
    "semestre": 5,
    "dificuldade": 5,
    "descricao": "Foca na construção e administração de portfólios. Estudo da Teoria Moderna de Carteiras (Markowitz), CAPM e Beta. Introduz métricas de controle como VaR e usa otimização matemática para selecionar ativos."
  },
  {
    "nome": "Análise de Séries Temporais para Finanças",
    "codigo": "FNA0022",
    "semestre": 5,
    "dificuldade": 5,
    "descricao": "Evolução da Econometria, foca em dados que variam cronologicamente (séries temporais). Desenvolvimento de modelos preditivos (ARIMA) e modelagem de volatilidade (GARCH). Essencial para análise quantitativa e previsões financeiras."
  },
  {
    "nome": "Finanças Corporativas I",
    "codigo": "FNA0024",
    "semestre": 6,
    "dificuldade": 4,
    "descricao": "Gestão financeira interna e estratégica. Estuda estrutura de capital, WACC e políticas de dividendos. Domínio de técnicas de análise de viabilidade de projetos (VPL e TIR) para maximizar o valor ao acionista."
  },
  {
    "nome": "Mercado de Capitais",
    "codigo": "FNA0025",
    "semestre": 6,
    "dificuldade": 4,
    "descricao": "Imersão profunda no funcionamento da Bolsa de Valores e SFN. Detalha negociação de ativos (ações, fundos), o papel da CVM e o processo de IPO (Abertura de Capital). Analisa o mercado como motor de financiamento."
  },
  {
    "nome": "Econometria para Finanças II",
    "codigo": "FNA0026",
    "semestre": 6,
    "dificuldade": 5,
    "descricao": "Aprofunda o uso de modelos estatísticos para análise de dados financeiros complexos. Foco em modelos de dados em painel e variáveis instrumentais para correção de endogeneidade. Inclui testes rigorosos de diagnóstico (heterocedasticidade e autocorrelação)."
  },
  {
    "nome": "Derivativos Financeiros",
    "codigo": "FNA0027",
    "semestre": 6,
    "dificuldade": 5,
    "descricao": "Estudo de instrumentos financeiros sofisticados (Opções, Futuros, Swaps, a Termo). Uso para estratégias de hedge e especulação. Domínio do modelo de precificação de Black-Scholes para avaliação de risco e proteção de carteiras."
  },
  {
    "nome": "Avaliação de Empresas",
    "codigo": "FNA0030",
    "semestre": 7,
    "dificuldade": 5,
    "descricao": "Conhecida como *Valuation*, foca em determinar o 'valor justo' de um negócio. Domínio do método do Fluxo de Caixa Descontado (FCD) e avaliações por múltiplos de mercado (P/L, EV/EBITDA) e baseadas em ativos. Essencial para fusões e aquisições."
  },
  {
    "nome": "Sistema Financeiro Nacional",
    "codigo": "FNA0031",
    "semestre": 7,
    "dificuldade": 3,
    "descricao": "Foco na arquitetura e regras do Sistema Financeiro Nacional (SFN). Estudo do papel do CMN, Banco Central, CVM, Copom (taxa Selic), regulação bancária e legislação, detalhando a dinâmica de bancos e corretoras."
  },
  {
    "nome": "Monografia I",
    "codigo": "FNA0032",
    "semestre": 7,
    "dificuldade": 4,
    "descricao": "Início do Trabalho de Conclusão de Curso (TCC). Foco na definição do tema, delimitação do problema, escrita da introdução e referencial teórico. Exige revisão bibliográfica profunda e rigor metodológico."
  },
  {
    "nome": "Finanças Internacionais",
    "codigo": "FNA0033",
    "semestre": 8,
    "dificuldade": 4,
    "descricao": "Expande para operações em múltiplas moedas e mercados globais. Detalha o funcionamento do mercado de câmbio, regimes cambiais e teorias de paridade. Foca em gerenciamento de risco cambial e o papel de instituições como FMI e Banco Mundial."
  },
  {
    "nome": "Monografia II",
    "codigo": "FNA0035",
    "semestre": 8,
    "dificuldade": 4,
    "descricao": "Finalização e defesa do Trabalho de Conclusão de Curso (TCC). Foco na coleta e análise de dados, aplicação da metodologia, redação de resultados/conclusões e revisão técnica (ABNT). Prepara para a defesa pública."
  }
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