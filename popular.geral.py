import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal_financas.settings')
django.setup()

from financeiro.models import Disciplina, Bolsa, LinkEssencial

print("Iniciando a automação de Links, Bolsas e Disciplinas...")


# 1. LINKS ESSENCIAIS DA UFC

links = [
    {"nome": "SIGAA", "descricao": "Coração da vida acadêmica. Matrículas, notas e histórico.", "url": "https://si3.ufc.br/sigaa/", "icone": "fas fa-graduation-cap"},
    {"nome": "Solar (AVA)", "descricao": "Plataforma para cursos semi-presenciais e materiais de aula.", "url": "https://solar.virtual.ufc.br/", "icone": "fas fa-sun"},
    {"nome": "Biblioteca Universitária", "descricao": "Catálogo Pergamum para reserva de livros.", "url": "https://biblioteca.ufc.br/", "icone": "fas fa-book"},
    {"nome": "Portal da PRAE", "descricao": "Editais de bolsas e auxílios para estudantes.", "url": "https://prae.ufc.br/", "icone": "fas fa-hand-holding-heart"},
    {"nome": "Restaurante Universitário (RU)", "descricao": "Cardápios, horários e recarga de créditos do RU.", "url": "https://www.ufc.br/restaurante/", "icone": "fas fa-utensils"},
]

criados_links = 0
for item in links:
    obj, created = LinkEssencial.objects.get_or_create(
        nome=item['nome'],
        defaults={'descricao': item['descricao'], 'url': item['url'], 'icone': item['icone']}
    )
    if created: criados_links += 1

# 2. BOLSAS E OPORTUNIDADES (Atualizado 2026)
bolsas = [
    {
        "nome": "Bolsa de Iniciação Acadêmica (BIA 2026)", 
        "valor": "R$ 700,00",
        "descricao": "Órgão: PRAE | Tipo: Auxílio estudantil.\nDestinada a estudantes de graduação presencial em situação de vulnerabilidade socioeconômica. Exige dedicação de 12 horas semanais. Não permite acúmulo.\nLink: https://prae.ufc.br/pt/edital-no-01-2026-prae-ufc-bolsa-de-iniciacao-academica/"
    },
    {
        "nome": "Programa de Iniciação à Docência (PID 2026)", 
        "valor": "Variável",
        "descricao": "Órgão: PROGRAD | Tipo: Monitoria.\nVoltada para alunos que desejam atuar como monitores auxiliando professores. Vagas remuneradas e voluntárias.\nLink: https://prograd.ufc.br/pt/edital-pid-no-19-2025-distribuicao-das-vagas-e-pontuacao-da-selecao-de-projetos-de-monitoria-de-iniciacao-a-docencia-em-2026/"
    },
    {
        "nome": "Programa de Bolsas de Extensão Universitária 2026", 
        "valor": "R$ 700,00",
        "descricao": "Órgão: PREX | Tipo: Extensão.\nAtuação em projetos que promovem a interação entre a universidade e a sociedade. Carga horária de 12h semanais.\nLink: https://prex.ufc.br/pt/prex-lanca-edital-do-programa-de-bolsas-de-extensao-universitaria-2026/"
    },
    {
        "nome": "Programa Institucional de Bolsas de Iniciação Científica (PIBIC 2025/2026)", 
        "valor": "R$ 700,00",
        "descricao": "Órgão: PRPPG | Tipo: Iniciação científica.\nDesperta a vocação científica atuando em projeto de pesquisa sob orientação de um professor.\nLink: https://prppg.ufc.br/pt/prppg-editais-pibic/"
    },
    {
        "nome": "Programa Bolsa de Incentivo ao Desporto 2026", 
        "valor": "Bolsa Atleta",
        "descricao": "Órgão: SESP-UFC / PRAE | Tipo: Auxílio estudantil.\nFomento à prática esportiva universitária. 100 vagas para representar a universidade em atividades desportivas.\nLink: https://desporto.ufc.br/pt/com-100-vagas-secretaria-de-esportes-da-ufc-sesp-ufc-e-pro-reitoria-de-assistencia-estudantil-prae-lancam-edital-para-o-programa-bolsa-de-incentivo-ao-desporto-2026/"
    },
    {
        "nome": "Auxílio Moradia", 
        "valor": "Ajuda de Custo",
        "descricao": "Órgão: PRAE | Tipo: Auxílio estudantil.\nDestinado a estudantes vulneráveis com famílias em municípios diferentes da sede do campus.\nLink: https://prae.ufc.br/pt/auxilio-moradia/"
    },
    {
        "nome": "Auxílio Creche", 
        "valor": "Ajuda de Custo",
        "descricao": "Órgão: PRAE | Tipo: Auxílio estudantil.\nPara estudantes (mães/pais) vulneráveis com filhos de 6 meses a 3 anos e 11 meses.\nLink: https://prae.ufc.br/pt/auxilio-creche/"
    },
    {
        "nome": "Isenção da Taxa do Restaurante Universitário (RU)", 
        "valor": "Isenção Total",
        "descricao": "Órgão: PRAE | Tipo: Auxílio estudantil.\nDireito de realizar as refeições (almoço e jantar) de forma totalmente gratuita nos refeitórios da UFC.\nLink: https://prae.ufc.br/pt/restaurante-universitario-ru/"
    },
    {
        "nome": "PIBITI (Desenvolvimento Tecnológico e Inovação)", 
        "valor": "R$ 700,00",
        "descricao": "Órgão: PRPPG / UFC Inova | Tipo: Iniciação científica.\nProjetos de pesquisa aplicada, desenvolvimento tecnológico e inovação.\nLink: https://prppg.ufc.br/pt/editais-pibiti/"
    },
    {
        "nome": "Programa de Promoção da Cultura Artística (Bolsa Arte)", 
        "valor": "R$ 700,00",
        "descricao": "Órgão: SECULT | Tipo: Extensão.\nParticipação em projetos artísticos e culturais aprovados pela SECULT. 12h semanais.\nLink: https://secult.ufc.br/pt/bolsa-arte/"
    },
    {
        "nome": "Bolsa de Iniciação Acadêmica para Estudantes com Deficiência (BIA-PCD)", 
        "valor": "R$ 700,00",
        "descricao": "Órgão: Secretaria de Acessibilidade / PRAE | Tipo: Auxílio estudantil.\nVagas específicas para estudantes PCD visando inclusão e permanência. 12h semanais.\nLink: https://acessibilidade.ufc.br/"
    }
]

criados_bolsas = 0
for item in bolsas:
    obj, created = Bolsa.objects.get_or_create(
        nome=item['nome'],
        defaults={'descricao': item['descricao'], 'valor': item['valor']}
    )
    if created: criados_bolsas += 1


disciplinas = [
    {"nome": "Introdução à Economia", "semestre": 1, "dificuldade": 3, "descricao": "Alicerces do pensamento econômico, micro e macroeconomia."},
    {"nome": "Matemática para Finanças I", "semestre": 1, "dificuldade": 5, "descricao": "Cálculo Diferencial aplicado, limites, derivadas e otimização de lucros."},
    {"nome": "Introdução à Contabilidade", "semestre": 1, "dificuldade": 4, "descricao": "Método das partidas dobradas, Balanço Patrimonial e DRE."},
    {"nome": "Metodologia do Trabalho Científico", "semestre": 1, "dificuldade": 2, "descricao": "Normas ABNT, pesquisa acadêmica e projetos científicos."},
    {"nome": "Matemática Financeira", "semestre": 2, "dificuldade": 4, "descricao": "Juros simples/compostos, SAC, Price, VPL e TIR."},
    {"nome": "Matemática para Finanças II", "semestre": 2, "dificuldade": 5, "descricao": "Integrais, derivadas parciais e otimização avançada."},
    {"nome": "Estatística para Finanças I", "semestre": 2, "dificuldade": 4, "descricao": "Estatística descritiva, probabilidades e distribuições."},
    {"nome": "Economia Brasileira para Finanças", "semestre": 2, "dificuldade": 3, "descricao": "História econômica do Brasil, Plano Real e crises."}
]

criados_disc = 0
for item in disciplinas:
    obj, created = Disciplina.objects.get_or_create(
        nome=item['nome'],
        defaults={'semestre': item['semestre'], 'dificuldade': item['dificuldade'], 'descricao': item['descricao']}
    )
    if created: criados_disc += 1

print(f"SUCESSO! Cadastrados: {criados_links} Links, {criados_bolsas} Bolsas, {criados_disc} Disciplinas.")