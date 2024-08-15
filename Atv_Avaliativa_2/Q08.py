'''
8. (Valor: 5 pontos) Na definição da Wikipédia, números triangulares são aqueles que representam o total 
de pontos que formam triângulos equiláteros em um plano (veja a definição detalhada em 
https://pt.wikipedia.org/wiki/Número_triangular).
Faça um programa que solicite ao usuário um número inteiro positivo e informe se ele é (ou não) triangular, 
de acordo com a definição.
'''

x = int(input('Digite o número que queira saber se é Triangular:'))

posicao = 0# vai demarcar a posição que a sequência dos números está

while True:
    t = posicao*(posicao+1)//2 # irá fazer a sequência de números triangulares
    if t == x: # se seu número estiver na sequência, é triangular. se não ele não é
        print('Seu número é triangular.')
        break
    elif t > x:
        print('Seu número não é triangular.')
        break
    posicao += 1