'''
Faça um programa que solicite ao usuário um valor decimal positivo (esse valor 
corresponde ao valor de um saque em um terminal de caixa eletrônico) e que calcule a quantidade de 
cédulas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e de moedas de R$ 1,00, R$ 
0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.
'''

saque = float(input('Informe quanto que irá ser sacado:(R$)'))

if saque > 0:
    Cedulas = int(round(saque, 2))
    Centavos = round(saque - Cedulas, 2)
    Cedulas100 = Cedulas // 100
    Cedulas = Cedulas % 100
    Cedulas50 = Cedulas // 50
    Cedulas = Cedulas % 50
    Cedulas20 = Cedulas // 20
    Cedulas = Cedulas % 20
    Cedulas5 = Cedulas // 5
    Cedulas = Cedulas % 5
    Cedulas2 = Cedulas // 2
    Cedulas = Cedulas % 2

    Moeda1 = Cedulas
    Moeda2 = Centavos // 0.50
    Centavos = round(Centavos % 0.50, 2)
    Moeda3 = Centavos // 0.25
    Centavos = round(Centavos % 0.25, 2)
    Moeda4 = Centavos // 0.10
    Centavos = round(Centavos % 0.10, 2)
    Moeda5 = Centavos // 0.05
    Centavos = round(Centavos % 0.05, 2)
    Moeda6 = Centavos * 100
    print(f'Notas de R$100: {Cedulas100},')
    print(f'Notas de R$50: {Cedulas50},') 
    print(f'Notas de R$20: {Cedulas20},') 
    print(f'Notas de R$5: {Cedulas5},')
    print(f'Notas de R$2: {Cedulas2}')

    print(f'Moedas de R$1,00: {Moeda1:0.0f},')
    print(f"Moedas de R$ 0,50: {Moeda2:0.0f},") 
    print(f"Moedas de R$ 0,25: {Moeda3:0.0f},") 
    print(f"Moedas de R$ 0,10: {Moeda4:0.0f},") 
    print(f"Moedas de R$ 0,05: {Moeda5:0.0f},") 
    print(f"Moedas de R$ 0,01: {Moeda6:0.0f}" )
else:
    print('Insira um valor válido')