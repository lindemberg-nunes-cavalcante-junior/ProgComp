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
import os

dirarquivo = os.path.abspath(__file__)
dirarquivo = os.path.dirname(dirarquivo)

arqentrada = open(dirarquivo + '\\CotacoesDolar2023.csv','r',encoding='utf-8')

while True:
    lista = arqentrada.readlines()

    if lista[-1] == '\n': lista

print(lista)