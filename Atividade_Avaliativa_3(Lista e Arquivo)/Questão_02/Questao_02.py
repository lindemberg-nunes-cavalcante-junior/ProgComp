'''
2. (Valor: 5 pontos) Faça um programa que leia dois valores: x e n (x e n deverão ser solicitados ao 
usuário), onde x é a quantidade de elementos que a lista deverá armazenar positivo e n serão os valores 
inteiros a serem inseridos na lista, o programa deve terminar a leitura dos números quando for informado 
o valor 0 (o valor 0 não deverá fazer parte da lista). A lista só deverá armazenar os x menores números 
informados, seguindo a lógica abaixo:
'''
import sys

x = int(input('Informe a quantidade de elementos da lista:'))

if x <= 0:
    sys.exit('Informe um valor maior que 0.')

lista = list()
n = 1

while n != 0:
    n = int(input('Informe um valor:'))
    
    if len(lista) < x:
        lista.append(n)
    elif lista[x-1] > n:
        lista[x-1] = n
    lista.sort()
    print(lista)