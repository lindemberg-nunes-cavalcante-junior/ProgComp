'''
5. (Valor: 5 pontos) Faça um programa que solicite ao usuário um valor inteiro positivo e informe a 
quantidade de dígitos.
ATENÇÃO: Não usar a função LEN().
Exemplo:
Informe um valor inteiro: 14583
O valor informado possui 5 dígitos
'''

numero = input('Informe um número:')
contado = 0
while numero[0:contado] != numero: 
        contado += 1
print(contado)

