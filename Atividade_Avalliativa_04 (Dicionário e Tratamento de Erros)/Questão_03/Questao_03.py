import random,sys
from Funcoes import Funcoes03

dictCartelas = dict()

while True:
    print('1. Gerar Cartela')
    print('2. Salvar Cartela')
    print('3. Ler Cartelas')
    print('4. Imprimir Cartela')
    print('5. Sair do programa')
    valor = int(input('informe a opção:'))
    if valor == 1:
        quantidade = int(input('Quantas cartelas serão geradas? '))
        dictCartelas = Funcoes03.Cartelas(quantidade)
    elif valor == 2:
        print(Funcoes03.SalvarC(dictCartelas))
    elif valor == 3:
        print()
    elif valor == 4:
        print()
    elif valor == 5: break