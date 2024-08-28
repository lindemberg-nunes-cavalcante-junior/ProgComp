'''
7. (Valor: 15 pontos) A partir do arquivo alunos_ifrn.csv, fazer um programa que:
a) Montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista 
deverá ser a sigla do campus e a segunda a quantidade de alunos daquele campus, no final deverá 
adicionada a cada sub-lista o percentual correspondente de alunos do campus em relação ao total de 
alunos do IFRN (limitar a 2 casas decimais). Essa lista deverá ser salva em um arquivo chamado 
alunos_ifrn_campus.csv (esse arquivo deverá ser salvo no mesmo diretório/pasta do programa). 
onde cada linha deverá ser os dados de cada sub-lista separados por ;;

b) Montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista 
deverá ser o ano de ingresso do aluno e a segunda posição a quantidade de alunos que ingressaram 
naquele ano. Essa lista deverá ser salva em um arquivo chamado alunos_ifrn_ano.csv (esse arquivo 
deverá ser salvo no mesmo diretório/pasta do programa). onde cada linha deverá ser os dados de 
cada sub-lista separados por ;;

c) Liste os campus, peça ao usuário para escolher um e montar uma segunda lista onde cada posição 
deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser o nome do curso e a 
segunda posição deverá ser quantidade de alunos daquele curso naquele campus. Essa lista deverá 
ser salva em um arquivo chamado alunos_ifrn_campus_curso.csv (esse arquivo deverá ser salvo 
no mesmo diretório/pasta do programa). onde cada linha deverá ser os dados de cada sub-lista 
separados por ;;
'''
import os

direntrada = os.path.abspath(__file__)
direntrada = os.path.dirname(direntrada)

arqentrada = open(direntrada + '\\alunos_ifrn.csv','r',encoding='utf-8')

listaentrada = [i[:-1].split(';') for i in arqentrada if i[-1:] =='\n' ]
