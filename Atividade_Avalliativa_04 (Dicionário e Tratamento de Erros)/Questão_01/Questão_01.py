import requests,sys, statistics
from datetime import datetime

try:
    strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata' 
    strURL += '/Moedas?$top=100&$format=json' 
    dictMoedas = requests.get(strURL).json()
except:
    print(f'/ERROR: {sys.exc_info()}') 




for i in dictMoedas['value']:
    x = i['simbolo']
    print(f'{x}')
moeda = input(f'Digite a moeda escolhida: ')
moedas = list(filter(lambda x: x['simbolo'] == moeda, dictMoedas['value']))
if len(moedas) <= 0:
    sys.exit('Moeda não existe')

ano = int(input('Digite o ano desejado: '))
if ano > int(datetime.now().year):
    sys.exit('Coloque um ano válido e anterior, ou igual, ao atual.')

meses = ['janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

media_compra = list()
media_venda = list()  

for i in range(1,13):

    if i < 10:
        try:
            strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/' 
            strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=' 
            strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?' 
            strURL += f'@moeda=%27{moeda}%27&@dataInicial=%2701-0{i}-{ano}%27&' 
            strURL += f'@dataFinalCotacao=%2712-31-{ano}%27&$top=100&$format=json' 
            dictCotacoes = requests.get(strURL).json()
        except:
            print(f'/ERROR: {sys.exc_info()}')
    else:
        try:
            strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/' 
            strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=' 
            strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?' 
            strURL += f'@moeda=%27{moeda}%27&@dataInicial=%2701-{i}-{ano}%27&' 
            strURL += f'@dataFinalCotacao=%2712-31-{ano}%27&$top=100&$format=json' 
            dictCotacoes = requests.get(strURL).json()
        except:
            print(f'/ERROR: {sys.exc_info()}')  
    media_compra.append(list(map(lambda x: [x['cotacaoCompra'], datetime.strptime(x['dataHoraCotacao'],"%Y-%m-%d %H:%M:%S.%f")],dictCotacoes['value'])))
    media_venda.append(list(map(lambda x: [x['cotacaoVenda'], datetime.strptime(x['dataHoraCotacao'],"%Y-%m-%d %H:%M:%S.%f")], dictCotacoes['value'])))


Cotas = {value: {'MediaCompra':[x[1].month for x in compra], 'MediaVenda':[x[1].month for x in venda]} for value,i,compra,venda in zip(meses,range(1,13),media_compra,media_venda)}

for i in Cotas.keys():
    print(f'{i}:{Cotas[i]['MediaCompra']}')


