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
            {"nome": "Matemática para Finanças I", "semestre": 1, "dificuldade": 5, "descricao": "Diferente da matemática financeira tradicional, esta cadeira foca no Cálculo Diferencial aplicado, fornecendo as ferramentas matemáticas essenciais para modelar variações de lucro, custo e receita. O percurso acadêmico inicia com a modelagem de funções reais voltadas ao comportamento organizacional, avança pelo estudo de limites e continuidade para a compreensão de mudanças instantâneas em variáveis econômicas e culmina na aplicação prática de derivadas. O ponto central da disciplina é a otimização, capacitando o estudante a encontrar pontos de lucro máximo e custo mínimo em diversas operações financeiras e de mercado."},
            {"nome": "Introdução à Contabilidade", "semestre": 1, "dificuldade": 4, "descricao": "Considerada a porta de entrada para interpretar a saúde financeira de qualquer organização, esta disciplina foca nas técnicas de registro e na estrutura fundamental dos relatórios contábeis. O estudante dominará o Método das Partidas Dobradas, onde a lógica de débito e crédito garante o equilíbrio das contas, e aprenderá a organizar o Plano de Contas entre Ativos, Passivos e Patrimônio Líquido. A parte prática envolve a montagem e análise crítica das principais demonstrações financeiras, como o Balanço Patrimonial e a Demonstração do Resultado do Exercício (DRE), ferramentas vitais para identificar a rentabilidade real de um negócio."},
            {"nome": "Metodologia do Trabalho Científico", "semestre": 1, "dificuldade": 2, "descricao": "Esta disciplina estratégica visa transformar a escrita acadêmica em uma produção de alto nível, rigorosa e organizada. O conteúdo explora as diferenças entre o senso comum e o rigor do método científico, orientando o aluno na curadoria de fontes confiáveis em bases como Google Acadêmico e Scielo para evitar o plágio. Além do domínio técnico das Normas ABNT para citações e referências, o curso guia o estudante na estruturação completa de trabalhos acadêmicos — de resumos e resenhas à elaboração de projetos de pesquisa que incluam problemas, hipóteses, objetivos e justificativas científicas sólidas."},
            {"nome": "Matemática Financeira", "semestre": 2, "dificuldade": 4, "descricao": "Esta disciplina constitui a base prática fundamental do curso, capacitando o aluno a dominar o conceito de valor do dinheiro no tempo e as operações do mercado financeiro. O conteúdo abrange o estudo aprofundado de juros simples e compostos, a diferenciação entre taxas nominais e efetivas, e o funcionamento detalhado dos principais sistemas de amortização, como as Tabelas SAC e Price. Além disso, o estudante aprenderá a projetar fluxos de caixa e utilizar ferramentas de análise de viabilidade de investimentos, como o Valor Presente Líquido (VPL) e a Taxa Interna de Retorno (TIR), essenciais para a tomada de decisão empresarial."},
            {"nome": "Matemática para Finanças II", "semestre": 2, "dificuldade": 5, "descricao": "Continuação direta do cálculo diferencial iniciado no semestre anterior, esta cadeira aprofunda as ferramentas matemáticas necessárias para modelos econômicos complexos. O foco principal é o estudo de integrais — operação inversa da derivada usada para acumulação de valores e cálculo de áreas sob curvas de funções financeiras — além da introdução às funções de várias variáveis. O aluno dominará derivadas parciais e técnicas avançadas de otimização aplicadas a cenários reais, onde é necessário maximizar resultados ou minimizar custos sob múltiplas restrições financeiras e operacionais."},
            {"nome": "Estatística para Finanças I", "semestre": 2, "dificuldade": 4, "descricao": "Esta disciplina introduz o aluno ao universo da análise de dados, fornecendo a base estatística necessária para prever riscos e retornos no mercado financeiro global. O percurso acadêmico envolve o domínio da estatística descritiva, incluindo medidas de tendência central como média, moda e mediana, e medidas de dispersão como desvio padrão e variância. O conteúdo avança para a teoria das probabilidades, distribuições de frequência e o estudo da correlação entre diferentes variáveis econômicas, preparando o estudante para interpretar amostragens e fundamentar decisões em dados concretos."},
            {"nome": "Economia Brasileira para Finanças", "semestre": 2, "dificuldade": 3, "descricao": "Com um caráter mais teórico e histórico, esta cadeira foca na análise crítica da realidade econômica do Brasil e sua evolução ao longo do tempo. O curso explora desde os grandes ciclos históricos da nossa economia até os modernos planos de estabilização, com ênfase especial na implementação e nos impactos do Plano Real. São discutidos temas vitais como o histórico das crises econômicas nacionais, a evolução da dívida pública, as reformas estruturais e os desafios do cenário atual do mercado nacional frente à economia globalizada, permitindo uma compreensão profunda do ambiente onde o profissional de finanças irá atuar."},
            {"nome": "Microeconomia I", "semestre": 3, "dificuldade": 4, "descricao": "Esta disciplina aprofunda a análise do comportamento dos agentes econômicos, focando na tomada de decisão de consumidores e firmas. O conteúdo explora a fundo as curvas de indiferença e restrições orçamentárias, avançando para o estudo das funções de produção complexas, como a Cobb-Douglas. O aluno aprenderá a modelar estruturas de custos de curto e longo prazo, além de compreender a mecânica do equilíbrio em mercados perfeitamente competitivos. A cadeira exige uma forte base em álgebra aplicada a gráficos para explicar como as escolhas individuais ditam a formação de preços e quantidades na economia."},
            {"nome": "Macroeconomia I", "semestre": 3, "dificuldade": 4, "descricao": "Focada no estudo da economia em nível agregado, esta cadeira investiga as forças que determinam a riqueza de uma nação. O ponto central do curso é o domínio do Modelo IS-LM, que analisa o equilíbrio simultâneo entre o mercado de bens e o mercado monetário, além da introdução ao modelo de Oferta e Demanda Agregada. Através de modelagens teóricas, o estudante aprenderá como as variações nos gastos do governo e as alterações nas taxas de juros impactam diretamente o PIB nacional, preparando-o para interpretar as grandes oscilações e tendências das políticas governamentais."},
            {"nome": "Estatística para Finanças II", "semestre": 3, "dificuldade": 4, "descricao": "Nesta etapa, o curso migra da análise descritiva para a Estatística Inferencial, fornecendo as ferramentas matemáticas para validar se dados financeiros são estatisticamente relevantes ou meros acasos. O conteúdo abrange testes de hipóteses, intervalos de confiança e o domínio de distribuições específicas como t-Student e Qui-quadrado. A disciplina culmina na introdução à regressão linear simples, técnica fundamental para prever o comportamento de uma variável financeira com base em outra, sendo um passo essencial para quem deseja atuar com análise de riscos e modelos econométricos."},
            {"nome": "Álgebra Linear para Finanças", "semestre": 3, "dificuldade": 5, "descricao": "Considerada uma das disciplinas mais desafiadoras e abstratas do curso, a Álgebra Linear fornece a base matemática para o gerenciamento moderno de carteiras de investimentos. Através do estudo de vetores, matrizes, sistemas de equações e transformações lineares, o aluno desenvolve o raciocínio necessário para lidar com múltiplos ativos simultâneos em um portfólio. O programa inclui ainda conceitos avançados de autovalores e autovetores, ferramentas que, apesar de teóricas, são indispensáveis para a computação financeira e a modelagem de grandes volumes de dados econômicos."},
            {"nome": "Econometria I para Finanças", "semestre": 0, "dificuldade": 4, "descricao": "Esta disciplina é o divisor de águas que une teoria econômica, matemática e estatística para testar hipóteses com dados reais do mercado. O conteúdo foca no Modelo de Regressão Linear Múltipla, ensinando o aluno a isolar o efeito de diversas variáveis sobre um indicador financeiro. Você aprenderá a identificar e corrigir problemas complexos como a heterocedasticidade e a autocorrelação, garantindo que as previsões e modelos econométricos sejam estatisticamente válidos para a tomada de decisão profissional."},
            {"nome": "Finanças Corporativas I", "semestre": 0, "dificuldade": 4, "descricao": "Voltada para a gestão interna das organizações, esta cadeira explora como as empresas tomam decisões estratégicas de investimento e financiamento. O estudo abrange a análise de estrutura de capital, o custo médio ponderado de capital (WACC) e as políticas de dividendos. O estudante será capacitado a avaliar o valor de projetos e empresas através de métricas de retorno e risco, entendendo como maximizar o valor para o acionista enquanto mantém a saúde financeira e a liquidez da firma no longo prazo."},
            {"nome": "Mercado de Capitais", "semestre": 0, "dificuldade": 3, "descricao": "Uma imersão no funcionamento prático da Bolsa de Valores e dos sistemas financeiros globais. A disciplina detalha a dinâmica de emissão e negociação de ações, debêntures e títulos públicos, além de introduzir o funcionamento dos mercados de derivativos e contratos futuros. O foco é compreender como o mercado de capitais serve como motor de captação de recursos para as empresas e como plataforma de investimento para indivíduos, analisando o papel de corretoras, bancos de investimento e órgãos reguladores como a CVM."},
            {"nome": "Gestão de Riscos", "semestre": 0, "dificuldade": 4, "descricao": "Fundamental para o setor bancário e de investimentos, esta disciplina ensina a identificar, medir e mitigar as incertezas que afetam os ativos financeiros. O conteúdo aborda os principais tipos de riscos — de mercado, de crédito, operacional e de liquidez — utilizando ferramentas estatísticas avançadas como o Value at Risk (VaR). O aluno aprenderá a utilizar instrumentos de hedge e estratégias de diversificação para proteger portfólios contra oscilações severas e crises sistêmicas, garantindo a resiliência das operações financeiras."},
            {"nome": "Microeconomia II", "semestre": 0, "dificuldade": 4, "descricao": "Esta disciplina expande o olhar econômico para além da competição perfeita, mergulhando nas complexidades e falhas do mercado real. O curso foca intensamente na Teoria dos Jogos, explorando estratégias de decisão em cenários de interdependência, e analisa modelos de Oligopólio (como Cournot e Bertrand) e Monopólio. O estudante aprenderá como as externalidades e a informação assimétrica — situações onde uma parte detém mais conhecimento que a outra — impactam diretamente os negócios e a eficiência dos mercados, fornecendo uma base sólida para a análise estratégica e a modelagem matemática de decisões competitivas."},
            {"nome": "Métodos Computacionais Aplicados às Finanças", "semestre": 0, "dificuldade": 4, "descricao": "Onde a tecnologia e as finanças se fundem, transformando linguagens como Python ou R em ferramentas essenciais de trabalho. O aluno aprenderá a automatizar cálculos financeiros complexos, realizar Simulações de Monte Carlo para a previsão de riscos e manipular grandes bases de dados (Big Data). O foco é o desenvolvimento de competências em programação aplicada para a criação de algoritmos de otimização de carteiras e a automação de processos, preparando o profissional para as exigências analíticas e tecnológicas do mercado financeiro moderno."},
            {"nome": "Econometria para Finanças I", "semestre": 0, "dificuldade": 4, "descricao": "Considerada o grande pilar analítico do curso, esta cadeira une Economia, Matemática e Estatística para validar hipóteses com rigor científico. O foco central é a construção e interpretação de modelos de Regressão Linear Múltipla, permitindo entender como diversas variáveis — como taxas de juros, inflação e câmbio — influenciam simultaneamente o preço de ativos ou indicadores econômicos. A disciplina inclui testes de diagnóstico avançados para identificar problemas como heterocedasticidade, garantindo que os modelos criados sejam confiáveis e robustos para projeções financeiras."},
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