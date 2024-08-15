'''
Em um estacionamento, as tarifas são as seguintes (cumulativas):
• Até duas horas: R$ 8,00/hora ou fração;
• Entre três e quatro horas: R$ 5,00/hora ou fração;
• Horas seguintes: R$ 3,00/hora ou fração.
• Depois de 12h, o custo passa a ser fixo: R$ 30,00
Faça um programa que leia o número de minutos que um veículo permaneceu no estacionamento e exiba 
o valor a ser pago pelo responsável.
Como exemplo, considere que o carro ficou 310 minutos no estacionamento; deve pagar: R$ 16,00 (pelas 
duas primeiras horas) + R$ 10,00 (pela terceira e quarta horas) + R$ 6,00 (pela quinta hora e fração da 
sexta hora): total de R$ 32,00
'''

M = int(input('Informe quantos minutos se passou:'))

horas = M/60
horas_totais = int(round(horas, 0))
fracao = horas - horas_totais


if horas > 2:
    if horas > 2 and horas <= 4:
        if fracao > 0:
            intervalo = 10 + 16
        elif fracao == 0:
            intervalo = 16 + 5
    elif horas >= 5 and horas < 12:
        horas = horas - 4
        horas_totais = int(round(horas, 0))
        intervalo = (horas_totais * 6) + 10 + 16
    elif horas >= 12:
        intervalo = 30
elif fracao > 0:
    intervalo = 16
else:
    intervalo = 8
intervalo = float(intervalo)
print(f'No total ficou R${intervalo:0.2f} a pagar.')


