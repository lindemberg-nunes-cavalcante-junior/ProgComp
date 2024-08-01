'''
9. (Valor: 5 pontos) Na definição da Wikipedia, número de Armstrong é aquele número cuja soma de cada 
digito dele elevado a potência n (onde n é a quantidade de dígitos) é igual ao número informado (veja a 
definição detalhada em https://en.wikipedia.org/wiki/Narcissistic_number).
Faça um programa que solicite ao usuário um número inteiro positivo e informe se ele é (ou não) um 
número de Armstrong, de acordo com a definição. NÃO usar a função LEN().
'''
import sys

x = input('Digite seu número de Armstrong:')
if int(x) < 0:
     sys.exit('Este número precisa ser positivo e inteiro')


soma = 0
contado = 0

while x[0:contado] != x: #contando o número de dígitos
        contado += 1

x = int(x)
aux = x
while True:
    if x > 0:
        soma += (x%10) ** contado
        x = x//10
    else:
        soma += x**contado
        break

if soma == aux:
    print('Seu número é de Armstrong.')
else:
     print('Seu número não é de Armstrong.')
    
