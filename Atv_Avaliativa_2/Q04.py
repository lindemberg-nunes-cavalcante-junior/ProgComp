'''
4. (Valor: 5 pontos) Existem somente quatro números, maiores do que um, que podem ser obtidos pela
soma de potências de 4 dos seus dígitos:
1643 = 14 + 64 + 44 + 34
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
Faça um programa que encontra e exibe os números menores de 1000000, que são múltiplos de 2 ou 5
e que podem ser escritos pela soma das potências de 5 de seus dígitos.
'''
b = 0
resposta = ''
for i in range(10000):
    #if i%2 == 0 or i%4 == 0:
    a = str(i)
    for c in range(len(a)):
        aux = int(a[c])
        b += aux**4
        if b == a:
            print(b)