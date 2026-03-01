import os
import django

# Avisa o script de onde puxar as configurações do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal_financas.settings')
django.setup()

from financeiro.models import TermoFinanceiro

termos = [
    {"termo": "Ativo", "definicao": "Conjunto de bens e direitos controlados por uma entidade, dos quais se esperam benefícios económicos futuros."},
    {"termo": "Passivo", "definicao": "Conjunto de obrigações e dívidas de uma empresa para com terceiros, exigindo a entrega de ativos ou prestação de serviços no futuro."},
    {"termo": "Patrimônio Líquido", "definicao": "Diferença entre o valor dos ativos e dos passivos de uma entidade, representando o capital próprio dos acionistas ou sócios."},
    {"termo": "Balanço Patrimonial", "definicao": "Demonstração contabilística que apresenta a posição financeira e económica de uma empresa num determinado momento."},
    {"termo": "DRE (Demonstração do Resultado do Exercício)", "definicao": "Relatório contabilístico que evidencia se a empresa teve lucro ou prejuízo num determinado período, detalhando receitas, custos e despesas."},
    {"termo": "Fluxo de Caixa", "definicao": "Registo de todas as entradas e saídas de dinheiro do caixa de uma empresa num período específico."},
    {"termo": "Capital de Giro", "definicao": "Recursos financeiros que a empresa precisa para manter as suas operações diárias a funcionar (pagar fornecedores, salários, etc.)."},
    {"termo": "EBITDA", "definicao": "Lucros antes de juros, impostos, depreciação e amortização. Mede a capacidade de geração de caixa operacional da empresa."},
    {"termo": "EBIT", "definicao": "Lucro antes dos juros e impostos. Representa o resultado puramente operacional da empresa."},
    {"termo": "ROI (Return on Investment)", "definicao": "Retorno sobre o Investimento. Métrica que indica o quanto a empresa ganhou ou perdeu em relação ao valor investido."},
    {"termo": "ROE (Return on Equity)", "definicao": "Retorno sobre o Patrimônio Líquido. Mede a rentabilidade que a empresa gera com o dinheiro dos próprios acionistas."},
    {"termo": "Margem Bruta", "definicao": "Percentagem de lucro que a empresa obtém após deduzir os custos diretos associados à produção dos bens ou serviços vendidos."},
    {"termo": "Margem Líquida", "definicao": "Percentagem de lucro que resta de cada unidade de venda após todas as despesas, impostos e custos terem sido deduzidos."},
    {"termo": "Amortização", "definicao": "Redução gradual do valor de uma dívida através de pagamentos periódicos ou a perda de valor de ativos intangíveis ao longo do tempo."},
    {"termo": "Insolvência", "definicao": "Situação em que uma pessoa ou empresa tem mais dívidas do que bens e não consegue cumprir com os seus compromissos financeiros."},
    {"termo": "Falência", "definicao": "Processo legal em que é declarada a incapacidade de uma empresa pagar as suas dívidas, resultando no encerramento das suas atividades e venda de bens para pagar aos credores."},
    {"termo": "Recuperação Judicial", "definicao": "Medida legal que visa evitar a falência de uma empresa, permitindo-lhe renegociar as suas dívidas enquanto continua a operar."},
    {"termo": "Ações Ordinárias (ON)", "definicao": "Ações que conferem ao acionista o direito de voto nas assembleias da empresa."},
    {"termo": "Ações Preferenciais (PN)", "definicao": "Ações que não dão direito a voto, mas oferecem preferência no recebimento de dividendos e no reembolso de capital em caso de liquidação."},
    {"termo": "Debêntures", "definicao": "Títulos de dívida emitidos por empresas de capital aberto para captar recursos no mercado, pagando juros aos investidores."},
    {"termo": "FIIs (Fundos de Investimento Imobiliário)", "definicao": "Fundos formados por grupos de investidores com o objetivo de aplicar recursos no mercado imobiliário."},
    {"termo": "LCI (Letra de Crédito Imobiliário)", "definicao": "Título de renda fixa emitido por bancos para financiar o setor imobiliário, isento de imposto de renda para pessoas físicas."},
    {"termo": "LCA (Letra de Crédito do Agronegócio)", "definicao": "Título de renda fixa emitido por bancos para financiar o setor agrícola, também isento de imposto de renda para pessoas físicas."},
    {"termo": "Renda Fixa", "definicao": "Tipo de investimento onde as regras de remuneração são conhecidas no momento da aplicação."},
    {"termo": "Renda Variável", "definicao": "Investimento em que a rentabilidade não é garantida nem conhecida à partida, podendo variar positivamente ou negativamente, como nas ações."},
    {"termo": "Dividendos", "definicao": "Parcela do lucro líquido de uma empresa distribuída aos seus acionistas na proporção das ações que possuem."},
    {"termo": "JCP (Juros sobre Capital Próprio)", "definicao": "Forma de distribuição de lucros aos acionistas, semelhante aos dividendos, mas tratada como despesa para a empresa, gerando benefício fiscal."},
    {"termo": "Ibovespa", "definicao": "Principal índice de desempenho das ações negociadas na B3, reunindo as empresas mais importantes e negociadas do mercado de capitais brasileiro."},
    {"termo": "B3 (Brasil, Bolsa, Balcão)", "definicao": "A bolsa de valores oficial do Brasil, sediada em São Paulo, onde são negociadas ações, títulos e derivativos."},
    {"termo": "Corretora de Valores", "definicao": "Instituição financeira que atua como intermediária na compra e venda de ativos financeiros no mercado de capitais."},
    {"termo": "CVM (Comissão de Valores Mobiliários)", "definicao": "Autarquia federal responsável por fiscalizar, regulamentar e desenvolver o mercado de valores mobiliários no Brasil."},
    {"termo": "Risco de Crédito", "definicao": "Probabilidade de o emitente de um título ou devedor não cumprir com o pagamento de juros ou do valor principal (calote)."},
    {"termo": "Risco de Mercado", "definicao": "Risco de perdas devido a oscilações nos preços dos ativos, taxas de juros ou taxas de câmbio."},
    {"termo": "Risco de Liquidez", "definicao": "Dificuldade de vender um ativo rapidamente a um preço justo por falta de compradores no mercado."},
    {"termo": "Spread Bancário", "definicao": "Diferença entre a taxa de juros que o banco cobra ao emprestar dinheiro e a taxa que ele paga aos investidores que lhe confiam os seus fundos."},
    {"termo": "Taxa de Câmbio", "definicao": "Preço de uma moeda estrangeira medido em unidades da moeda nacional (ex: quantos Reais são precisos para comprar um Dólar)."},
    {"termo": "PTAX", "definicao": "Taxa de câmbio calculada pelo Banco Central do Brasil, que serve de referência para diversas operações no mercado financeiro."},
    {"termo": "Derivativos", "definicao": "Contratos financeiros cujo valor deriva do preço de um ativo subjacente (como ações, moedas ou commodities)."},
    {"termo": "Mercado Futuro", "definicao": "Ambiente da bolsa de valores onde são negociados contratos de compra e venda de ativos para uma data futura, com preço previamente acordado."},
    {"termo": "Commodities", "definicao": "Matérias-primas ou produtos básicos em estado bruto (como petróleo, soja, ouro) negociados globalmente com preços padronizados."}
]

print("Iniciando a inserção de termos no banco de dados...")
criados = 0

for item in termos:
    obj, created = TermoFinanceiro.objects.get_or_create(
        termo=item['termo'],
        defaults={'definicao': item['definicao']}
    )
    if created:
        criados += 1
        print(f"Adicionado: {item['termo']}")

print(f"SUCESSO! {criados} novos termos foram adicionados ao banco de dados da nuvem.")