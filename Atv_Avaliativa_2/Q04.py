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

for i in range(1,1000000 +1):
    if i%2 == 0 or i%5 == 0:
        a = str(i)
        for c in range(len(a)): #não sei dizer porque está dando print em 4150 duas vezes
            b += int(a[c])**5
            if int(a) == 4150:
                print(b)
            if str(b) == str(a):
                print(b)
        b = 0
            