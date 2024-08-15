'''
O número de dias decorridos entre duas datas é importante em uma infinidade de 
situações da vida cotidiana. Faça um programa que recebe inicialmente dois valores (dia inicial e mês 
inicial), depois mais dois valores (dia final, mês final), ao final deve indicar quantos dias se passaram entre 
as datas (considere que o ano não é bissexto).
Exemplos: 
o 02 de 05 até 03 de 05 - 1 dia
o 27 de 04 até 03 de 05 - 6 dias
o 03 de 02 até 03 de 05 - 79 dias
Não esqueça de verificar se a data inicial é menor ou igual à data final.
Dica: conte o número de dias até cada uma das datas e subtraia esses números.
'''

D_inicial = int(input('Informe o dia inicial:'))
M_inicial = int(input('Informe o mês inicial:'))
D_final = int(input('Informe o dia final:'))
M_final = int(input('Informe o mês final:'))

if D_inicial <= D_final and M_inicial <= M_final:
    dias_começo = 0
    if M_inicial > 1:
        dias_começo += 31
    if M_inicial > 2:
        dias_começo += 28 
    if M_inicial > 3:
        dias_começo += 31  
    if M_inicial > 4:
        dias_começo += 30  
    if M_inicial > 5:
        dias_começo += 31  
    if M_inicial > 6:
        dias_começo += 30  
    if M_inicial > 7:
        dias_começo += 31  
    if M_inicial > 8:
        dias_começo += 31  
    if M_inicial > 9:
        dias_começo += 30  
    if M_inicial > 10:
        dias_começo += 31  
    if M_inicial > 11:
        dias_começo += 30
    dias_começo = dias_começo + D_inicial

    dias_final = 0
    if M_inicial > 1:
        dias_final += 31
    if M_inicial > 2:
        dias_final += 28 
    if M_inicial > 3:
        dias_final += 31  
    if M_inicial > 4:
        dias_final += 30  
    if M_inicial > 5:
        dias_final += 31  
    if M_inicial > 6:
        dias_final += 30  
    if M_inicial > 7:
        dias_final += 31  
    if M_inicial > 8:
        dias_final += 31  
    if M_inicial > 9:
        dias_final += 30  
    if M_inicial > 10:
        dias_final += 31  
    if M_inicial > 11:
        dias_final += 30
    dias_final = dias_final + D_final

    dias = dias_final - dias_começo               
    print(f'Se passaram {dias} dias')
        