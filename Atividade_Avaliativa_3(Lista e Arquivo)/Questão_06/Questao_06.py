'''
6. (Valor: 15 pontos) A partir do arquivo CotacoesDolar2023.csv, fazer um programa que: 
a) Monte uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista 
deverá ser o mês (Janeiro, Fevereiro,..., Dezembro), a segunda posição deverá ser a maior cotação 
de venda do respectivo mês e a terceira posição deverá ser a data relativa a essa maior cotação. 
b) Montar uma segunda lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada 
sub-lista deverá ser o mês (Janeiro, Fevereiro,..., Dezembro), e a segunda posição deverá ser a média 
das cotações de venda do respectivo mês; 
c) Teste depois para o arquivo CotacoesDolar2024.csv; 
ATENÇÃO:  
i) 
Nos arquivos CSV, a ordem das informações são: DATA, N/C, N/C, N/C, VALOR COMPRA, VALOR 
VENDA, N/C, N/C; 
ii) 
Deverão ser utilizadas as funções MAP(), SORT(), FILTER() e List Comprehensions quando 
possível.
'''
import os,statistics

dirarquivo = os.path.abspath(__file__)
dirarquivo = os.path.dirname(dirarquivo)

arqentrada = open(dirarquivo + '\\CotacoesDolar2023.csv','r',encoding='utf-8')

# listaentrada = [i[:-1].split(';') for i in arqentrada if i[-1:] == '\n']
listaentrada = [[float(i.split(';')[5].replace(',','.')),i.split(';')[0]] for i in arqentrada]
listaentrada.sort(key=lambda x: x[1][2:len(x)])
meses = [['janeiro'],['Fevereiro'],['Março'],['Abril'],['Maio'], ['Junho'],['Julho'],['Agosto'],['Setembro'],['Outubro'],['Novembro'],['Dezembro']]

for mes in range(1,13):
    listacotas = list(filter(lambda x: int(x[1][2:4]) == mes,listaentrada))
    
    if len(listacotas) > 0:
        listaMM = list(map(lambda x: [meses[mes], max(x),])) 