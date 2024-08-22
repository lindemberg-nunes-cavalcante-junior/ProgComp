'''
. (Valor: 15 pontos) Fazer um programa para gerar automaticamente uma lista de dimensão de n
elementos (n deverá ser solicitado ao usuário, positivo e entre 7 e 60, inclusive), cada elemento dessa 
lista será um número aleatório entre 1 e 60 (inclusive) sem repetição. Após a lista ser gerada, as seguintes 
operações deverão ser implementadas:
a) Deverá ser criada uma segunda lista com todas as combinações possíveis. Cada combinação deverá 
ser uma sub-lista. Cada combinação deverá estar ordenada do menor número para o maior;
b) A lista de números escolhidos deverá ser salva em um arquivo chamado numeros_escolhidos.txt
(salvar no mesmo diretório/pasta em que o programa está salvo). Nesse arquivo os números deverão 
estar em apenas 1 linha. Utilize ; para separar os valores na linha;
c) A lista de combinações deverá ser salva em um arquivo chamado combinações.txt (salvar no mesmo 
diretório/pasta em que o programa está salvo). Nesse arquivo cada combinação deverá estar em 1 
linha. Utilize ; para separar os valores na linha;
d) No final deverão ser exibidos na tela quantas combinações foram geradas, e quais as probabilidades
de se acertar a sena, a quina e a quadra.
'''
import sys,random

x = int(input('Digite um número de 7 e 60:'))

if x < 7 or x > 60:
    sys.exit('Digite um número na faixa pedida.')

lista = list(random.randint(1,60) for _ in range(x))

print(lista)