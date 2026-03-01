import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal_financas.settings')
django.setup()

from django.contrib.auth import get_user_model
from financeiro.models import TermoFinanceiro

print("Verificando administrador...")
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@email.com', 'Ufc12345')
    print("Usuário admin recriado com sucesso!")

termos = [
   {"termo": "PIB (Produto Interno Bruto)", "definicao": "Soma de todos os bens e serviços finais produzidos em uma determinada região, durante um período determinado."},
    {"termo": "RNB (Renda Nacional Bruta)", "definicao": "Soma de todas as rendas recebidas pelos residentes de um país, incluindo o saldo de rendas enviadas e recebidas do exterior."},
    {"termo": "PNB (Produto Nacional Bruto)", "definicao": "Valor de todos os bens e serviços finais produzidos por empresas de um país, independentemente de onde estejam operando no mundo."},
    {"termo": "PIB per capita", "definicao": "Indicador que divide o Produto Interno Bruto pela quantidade de habitantes de um país ou região, medindo a renda média por pessoa."},
    {"termo": "Valor Adicionado", "definicao": "Valor que cada setor da economia acrescenta aos bens intermediários consumidos no processo produtivo."},
    {"termo": "Consumo Intermediário", "definicao": "Valor dos bens e serviços consumidos no processo de produção de outros bens e serviços."},
    {"termo": "FBCF (Formação Bruta de Capital Fixo)", "definicao": "Medida do quanto as empresas aumentaram seus bens de capital (máquinas, equipamentos, construção civil) no período."},
    {"termo": "Variação de Estoques", "definicao": "Diferença entre o valor das entradas e saídas de produtos nos estoques das empresas durante um período."},
    {"termo": "Depreciação", "definicao": "Perda de valor de um bem de capital (máquinas, instalações) devido ao desgaste físico pelo uso ou obsolescência técnica."},
    {"termo": "RLEE (Renda Líquida Enviada ao Exterior)", "definicao": "Diferença entre a renda enviada a não residentes e a renda recebida do exterior por residentes do país."},
    {"termo": "Carga Tributária", "definicao": "Relação entre o total de impostos arrecadados pelo governo e o Produto Interno Bruto (PIB) do país."},
    {"termo": "Impostos Indiretos", "definicao": "Tributos que incidem sobre o consumo e a produção de bens e serviços, como o ICMS e o IPI."},
    {"termo": "Subsídios", "definicao": "Ajuda financeira concedida pelo governo a empresas ou setores econômicos para baratear a produção ou incentivar atividades."},
    {"termo": "Balança Comercial", "definicao": "Diferença entre o valor total das exportações e das importações de bens de um país."},
    {"termo": "Balanço de Pagamentos", "definicao": "Registro contábil de todas as transações econômicas entre os residentes de um país e o resto do mundo."},
    {"termo": "Taxa Selic", "definicao": "Taxa básica de juros da economia brasileira, definida pelo Copom, que serve de referência para as demais taxas de juros."},
    {"termo": "Copom", "definicao": "Comitê de Política Monetária do Banco Central do Brasil, responsável por definir a meta da Taxa Selic."},
    {"termo": "IPCA (Índice Nacional de Preços ao Consumidor Amplo)", "definicao": "Índice oficial medido pelo IBGE que acompanha a variação dos preços de um conjunto de produtos e serviços, medindo a inflação do país."},
    {"termo": "IGP-M", "definicao": "Índice Geral de Preços - Mercado, muito utilizado para o reajuste de contratos de aluguel e tarifas públicas."},
    {"termo": "Inflação", "definicao": "Aumento contínuo e generalizado do nível de preços de bens e serviços em uma economia, gerando a perda do poder de compra."},
    {"termo": "Deflação", "definicao": "Queda contínua e generalizada do nível de preços de bens e serviços, o inverso da inflação."},
    {"termo": "Política Monetária", "definicao": "Ações do Banco Central para controlar a quantidade de dinheiro em circulação e a taxa de juros da economia."},
    {"termo": "Política Fiscal", "definicao": "Decisões do governo sobre como arrecadar receitas (impostos) e como gastar esses recursos públicos."},
    {"termo": "Superávit Primário", "definicao": "Ocorre quando a arrecadação do governo é maior que os seus gastos (despesas), antes do pagamento dos juros da dívida pública."},
    {"termo": "Déficit Nominal", "definicao": "Resultado negativo das contas públicas quando as despesas totais, incluindo o pagamento dos juros da dívida, superam a arrecadação."},
    {"termo": "Dívida Pública", "definicao": "Soma de todos os empréstimos tomados pelo governo (interno e externo) para financiar seus déficits."},
    {"termo": "Tesouro Direto", "definicao": "Programa do Tesouro Nacional que permite a pessoas físicas comprarem títulos da dívida pública federal pela internet."},
    {"termo": "CDB (Certificado de Depósito Bancário)", "definicao": "Título de renda fixa emitido pelos bancos para captar dinheiro, pagando juros ao investidor no final do prazo."},
    {"termo": "CDI (Certificado de Depósito Interbancário)", "definicao": "Taxa de juros dos empréstimos diários feitos entre os bancos; serve de principal referência para a rentabilidade da renda fixa."},
    {"termo": "Liquidez", "definicao": "Facilidade e rapidez com que um ativo pode ser transformado em dinheiro vivo sem perda de valor."},
    {"termo": "Custo de Oportunidade", "definicao": "O valor daquilo que você renuncia ao fazer uma escolha econômica; a melhor alternativa deixada de lado."},
    {"termo": "Oferta", "definicao": "Quantidade de um bem ou serviço que os produtores estão dispostos a vender no mercado a um determinado preço."},
    {"termo": "Demanda", "definicao": "Quantidade de um bem ou serviço que os consumidores desejam e podem comprar a um determinado preço."},
    {"termo": "Elasticidade-Preço", "definicao": "Mede a sensibilidade da quantidade demandada ou ofertada de um bem frente a alterações no seu preço."},
    {"termo": "Monopólio", "definicao": "Estrutura de mercado em que há apenas um único fornecedor de um determinado produto ou serviço, sem substitutos próximos."},
    {"termo": "Oligopólio", "definicao": "Estrutura de mercado dominada por um pequeno número de grandes empresas que detêm a maior parte do controle das vendas."},
    {"termo": "Cartel", "definicao": "Acordo ilegal entre empresas do mesmo setor para fixar preços, dividir o mercado e eliminar a concorrência."},
    {"termo": "Lucro Líquido", "definicao": "O valor que sobra para a empresa após deduzir da receita total todos os custos, despesas, impostos e juros."},
    {"termo": "Custo Fixo", "definicao": "Despesas da empresa que não mudam independentemente da quantidade produzida ou vendida (ex: aluguel)."},
    {"termo": "Custo Variável", "definicao": "Despesas que aumentam ou diminuem de acordo com o volume de produção ou vendas (ex: matéria-prima)."},
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
    {"termo": "Commodities", "definicao": "Matérias-primas ou produtos básicos em estado bruto (como petróleo, soja, ouro) negociados globalmente com preços padronizados."},
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

print(f"SUCESSO! {criados} novos termos foram adicionados ao banco de dados da nuvem.")