'''
6. (Valor: 5 pontos) Dado que uma Progressão Geométrica (P.G.) é a uma sequência numérica cujo 
quociente (q) ou razão entre um número e outro (exceto o primeiro) é sempre igual. Vale lembrar que 
essa razão é sempre constante e pode ser qualquer número racional (positivos, negativos, frações) exceto 
o número zero (0).
Faça um programa que:
a) Solicite ao usuário um valor inteiro inicial e a razão da P.G.;
b) Solicite um novo valor inteiro positivo correspondente a quantidade de elementos da PG e exiba 
os valores dessa P.G.;
c) Informe se a P.G. é constante, oscilante, crescente ou decrescente
d) Calcule a soma dos elementos dessa P.G.;
e) Solicite um outro valor inteiro n correspondente a enésima posição de um elemento da P.G. e 
exibir o valor desse elemento.
'''

inicial = int(input('Informe o valor inicial:'))
razao = float(input('Informe a razão da P.G.:'))
tamanho = int(input('Informe o tamanho da P.G.:'))

elementos = inicial

soma = inicial * ((razao**tamanho) - 1)/razao - 1

for i in range(inicial, tamanho+inicial):
    print(elementos, end= ' ')
    elementos = elementos * razao
print()

if razao < 0:
    tipo = 'oscilante'
elif razao > 0 and inicial > 0:
    tipo = 'crescente'
elif razao > 0 and inicial < 0:
    tipo = 'decrescente'
else:
    tipo = 'constante'

print(f'É do tipo {tipo}')
print(f"A soma dos elementos é:{soma}")

posicao = int(input('Digite uma posição que queira saber o valor:'))

a = inicial * razao**posicao - 1

print(f'O valor é {a}')

        
