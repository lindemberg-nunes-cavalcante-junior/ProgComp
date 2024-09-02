import requests,sys, statistics
from datetime import datetime

try:
    strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata' 
    strURL += '/Moedas?$top=100&$format=json' 
    dictMoedas = requests.get(strURL).json()
except:
    print(f'\ERROR: {sys.exc_info()}') 




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

try:
    strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/' 
    strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=' 
    strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?' 
    strURL += f'@moeda=%27{moeda}%27&@dataInicial=%2701-01-{ano}%27&' 
    strURL += f'@dataFinalCotacao=%2712-31-{ano}%27&$top=100&$format=json' 
    dictCotacoes = requests.get(strURL).json()
except:
    print(f'\ERROR: {sys.exc_info()}')

media_compra = list(map(lambda x: x['cotacaoCompra'], dictCotacoes['value']))
media_venda = list(map(lambda x: x['cotacaoVenda'], dictCotacoes['value']))  

print(media_compra)


