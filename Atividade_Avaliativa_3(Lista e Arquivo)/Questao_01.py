'''
1. (Valor: 5 pontos) Desenvolva um programa que solicite ao usuário dois valores inteiros: o primeiro 
representando a quantidade de listas na matriz e o segundo indicando a quantidade de elementos em 
cada lista. Com base nesses valores, o programa deverá gerar aleatoriamente os elementos da matriz
(utilizar List Comprehensions), exibir a matriz original e, em seguida, calcular e apresentar a matriz 
transposta.
A matriz transposta de uma matriz M com m linhas e n colunas é obtida trocando as linhas pelas colunas 
e vice-versa, resultando em uma matriz Mt com n linhas e m colunas.
'''
import random

listas = int(input('Coloque o número de listas que deseja:'))
elementos = int(input('Coloque a quantidade de elementos que cada um terá:'))

matriz = [[random.randint(0,10) for i in range(elementos) ] for i in range(listas)]

matrizT = [[i[x] for i in matriz] for x in range(elementos)]

print(matriz)
print(matrizT)

