'''
7. (Valor: 5 pontos) Dado que uma Progressão Aritmética (P.A.) é uma sequência de números onde a 
diferença entre dois termos consecutivos é sempre a mesma e que essa diferença constante é chamada 
de razão da P.A.
Faça um programa que:
a) Solicite ao usuário um valor inteiro inicial e a razão da P.A.;
b) Solicite um novo valor inteiro positivo correspondente a quantidade de elementos da P.A. e exiba 
os valores dessa P.A.;
c) Informe se a P.A. é constante, crescente ou decrescente
d) Calcule a soma dos elementos dessa P.A.;
e) Solicite ao usuário um outro valor inteiro n correspondente a enésima posição de um elemento 
da P.A. e exibir o valor desse elemento.
'''

inicial = int(input('Informe o valor inicial:'))
razao = float(input('Informe a razão da P.A.:'))
tamanho = int(input('Informe o tamanho da P.A.:'))

elementos = inicial

soma = 0

for i in range(inicial, tamanho+inicial):
    print(elementos, end= ' ')
    soma += elementos
    elementos = elementos + razao
    
print('')

if razao > 0:
    tipo = 'crescente'
elif razao < 0:
    tipo = 'decrescente'
elif razao == 0:
    tipo = 'constante'

print(f'É do tipo {tipo}')
print(f"A soma dos elementos é:{soma}")

posicao = int(input('Digite uma posição que queira saber o valor:'))

a = inicial + ((posicao - 1) * razao)

print(f'O valor é {a}')