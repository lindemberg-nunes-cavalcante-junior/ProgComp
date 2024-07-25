'''
2. (Valor: 5 pontos) Dados dois números inteiros positivos, determinar o Máximo Divisor Comum (MDC) 
entre eles usando o Algoritmo de Euclides.
'''
import sys

A = int(input('informe um número positivo A:'))
B = int(input('informe um número positivo B:'))

if A < 0 or B < 0:
    sys.exit("Os dois necessitam ser positivos")

while A != 0 and B != 0:
    MDC = A%B
    A = B
    B = MDC

if A == 0:
    print(f"MDC:{B}")
elif B == 0:
    print(f"MDC:{A}")
