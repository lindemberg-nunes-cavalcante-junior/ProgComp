import requests,sys,statistics,json,os
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
# moeda = input(f'Digite a moeda escolhida: ')
moeda = 'USD'
moedas = list(filter(lambda x: x['simbolo'] == moeda, dictMoedas['value']))
if len(moedas) <= 0:
    sys.exit('Moeda não existe')

# ano = int(input('Digite o ano desejado: '))
ano = 2024
if ano > int(datetime.now().year):
    sys.exit('Coloque um ano válido e anterior, ou igual, ao atual.')

try:
    strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
    strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
    strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
    strURL += f'@moeda=%27{moeda}%27&@dataInicial=%2701-01-{ano}%27&'
    strURL += f'@dataFinalCotacao=%2712-31-{ano}%27&$format=json'
    dictCotacoes = requests.get(strURL).json()
except:
    print(sys.exc_info())

meses = ['janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

medias = list(map(lambda x: [x['cotacaoCompra'], x['cotacaoVenda'],datetime.strptime(x['dataHoraCotacao'],"%Y-%m-%d %H:%M:%S.%f")],dictCotacoes['value']))

# Guardando as medias em um dicionário, onde a chave é o mes correspondente
Medias = {value: {'MediaCompra':round((statistics.mean([x[0] if x[2].month == mes else 0 for x in medias])),5),'MediaVenda':round((statistics.mean([x[1] if x[2].month == mes else 0 for x in medias])),5)} for value,mes in zip(meses,range(1,13))}

# Salvando os arquivos
direntrada = os.path.abspath(__file__)
direntrada = os.path.dirname(direntrada)

# JSON
arqentrada = open(direntrada + f'\\medias_cotacoes_{moeda}_{ano}.json','w',encoding='utf-8')
json.dump(Medias,arqentrada,indent=6)
arqentrada.close()

#CVC
arqentrada = open(direntrada + f'\\medias_cotacoes_{moeda}_{ano}.cvs','w',encoding='utf-8')
arqentrada.write('moeda;mes;mediaCompra;mediaVenda;\n')
for i in Medias.keys():
    x = Medias[i]['MediaCompra']
    y = Medias[i]['MediaVenda']
    arqentrada.write(f'{moeda};{i};{x};{y}\n')
arqentrada.close()



