import os
import django

# Avisa o script de onde puxar as configurações do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal_financas.settings')
django.setup()

from financeiro.models import TermoFinanceiro

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
    {"termo": "Custo Variável", "definicao": "Despesas que aumentam ou diminuem de acordo com o volume de produção ou vendas (ex: matéria-prima)."}
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