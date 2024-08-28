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
listaentrada = [[float(i.split(';')[5].replace(',','.')),i.split(';')[0]] for i in arqentrada]
arqentrada.close()
listaentrada.sort(key=lambda x: x[1][2:len(x)])
meses = ['janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
arqentrada = open(dirarquivo + '\\Cotações2023.text','w',encoding='utf-8')

cotacaoMAX= list()
cotacaoMED = list()

for mes in range(1,13):
    listacotas = list(filter(lambda x: int(x[1][2:4]) == mes,listaentrada))
    
    if len(listacotas) > 0:
        Max = max(list(map(lambda x: x[0], listacotas)))
        Media = statistics.mean(list(map(lambda x: x[0], listacotas)))
        data = list(x[1] for x in listacotas if Max in x)
        
        cotacaoMAX.append([meses[mes-1], Max, data[0]])
        cotacaoMED.append([meses[mes-1],Media])

arqentrada.write('Maiores Cotações Mensais\n')
for i in cotacaoMAX:
    arqentrada.write(f'{i[0]} ...{i[1]} ...{i[2][0:3]}/{i[2][2:4]}/{i[2][4:len(i[2])]}\n')
arqentrada.write('\n')

arqentrada.write('Média das Cotações Mensais\n')
for i in cotacaoMED:
    arqentrada.write(f'{i[0]} ...{i[1]:.5f}\n')
arqentrada.close()
