import requests

strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata' 
strURL += '/Moedas?$top=100&$format=json' 
dictMoedas = requests.get(strURL).json() 
strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/' 
strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=' 
strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?' 
strURL += '@moeda=%27USD%27&@dataInicial=%2701-01-2023%27&' 
strURL += '@dataFinalCotacao=%2712-31-2023%27&$top=100&$format=json' 
dictCotacoes = requests.get(strURL).json() 



cotacoes = [i for i in dictCotacoes['value']]

moedas = [i for i in dictMoedas['value']]

print(cotacoes)


