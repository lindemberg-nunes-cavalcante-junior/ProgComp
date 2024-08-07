'''
Com base na nova legislação da Previdência Brasileira, regulamentada pela Lei 
Complementar nº 1354/2020 e pela Emenda à Constituição nº 49/2020, desenvolva um programa em 
Python que solicite as seguintes informações de uma pessoa:
• Sexo da pessoa (masculino/feminino).
• Data de nascimento da pessoa (no formato DD/MM/AAAA).
• Data de início da contribuição previdenciária da pessoa (no formato DD/MM/AAAA).
O programa deve então calcular e exibir a data em que a pessoa poderá se aposentar, considerando as 
seguintes regras:
• Aposentadoria por Idade:
o Homens podem se aposentar aos 65 anos de idade.
o Mulheres podem se aposentar aos 62 anos de idade.
o É necessário ter pelo menos 15 anos de contribuição.
• Aposentadoria por Tempo de Contribuição:
o Homens podem se aposentar após 35 anos de contribuição.
o Mulheres podem se aposentar após 30 anos de contribuição.
Implemente o programa em Python para calcular a data de aposentadoria e exibi-la como resultado.
'''
from datetime import *

sexo = input('informe seu sexo(masculino/feminino):')
dt_nasc = datetime.strptime(input('Informe sua data de nascimento (DD/MM/AAAA):'), '%d/%m/%Y').date()
dt_previdencia = datetime.strptime(input('Informe sua data de início de contribuição (DD/MM/AAAA):'), '%d/%m/%Y').date()
dt_today = datetime.today()

idade_minima = (dt_today.year - dt_nasc.year)
if dt_nasc.day < dt_today.day and dt_nasc.month >= dt_today.month:
    idade_minima = idade_minima - 1
print('------------------------------------------------------------------------------------------')
if idade_minima >= 18:
    if sexo == 'masculino':
        dt_aposentar = dt_nasc.replace(year= dt_nasc.year + 65)
        dt_contribuir = dt_previdencia.replace(year= dt_previdencia.year + 15)

        dt_prevfutura = dt_previdencia.replace(year= dt_previdencia.year + 35)
        dt_prevfutura = dt_previdencia.strftime('%d/%m/%Y')
        print(f'Por contribuição você poderá se aposentar na data {dt_prevfutura}')
    
        if dt_contribuir.year - dt_previdencia.year < 15:
            dt_aposentar = dt_aposentar.replace(year= dt_aposentar.year + (dt_contribuir.year - dt_previdencia.year))
            print(f'Por idade você poderá se aposentar na data {dt_aposentar}')
        else:
            print(f'Por idade você poderá se aposentar na data {dt_aposentar}')
    elif sexo == 'feminino':
        dt_aposentar = dt_nasc.replace(year= dt_nasc.year + 62)
        dt_contribuir = dt_previdencia.replace(year= dt_previdencia.year + 15)

        dt_prevfutura = dt_previdencia.replace(year= dt_previdencia.year + 30)
        dt_prevfutura = dt_previdencia.strftime('%d/%m/%Y')
        print(f'Por contribuição você poderá se aposentar na data {dt_prevfutura}')
    
        if dt_contribuir.year - dt_previdencia.year < 15:
            dt_aposentar = dt_aposentar.replace(year= dt_aposentar.year + (dt_contribuir.year - dt_previdencia.year))
            print(f'Por idade você poderá se aposentar na data {dt_aposentar}')
        else:
            print(f'Por idade você poderá se aposentar na data {dt_aposentar}')
else:
    print('Você não possui a idade mínima para contribuir.')