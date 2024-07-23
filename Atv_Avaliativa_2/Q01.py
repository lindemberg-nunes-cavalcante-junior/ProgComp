'''
1. (Valor: 5 pontos) Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Faça um programa que solicite a massa inicial (em gramas) e que calcule o tempo necessário para que 
essa massa se torne menor que 0,5 grama. Ao término, o programa deve exibir a massa inicial, a massa 
final e o tempo que levou para o decaimento (exiba o tempo informando horas, minutos e segundos).
Exemplo de saída:
Massa Inicial: 250 gramas
Massa Final: 0.48828125 gramas
Tempo de Decaimento: 0:07:30

'''
import sys

massa = float(input('Digite a massa que irá decair (positivo):'))
massa_inicial = massa # salvando a massa inicial

if massa < 0:
    sys.exit("A massa necessita ser maior que isso.")

time = 0 # este tempo irá marcar os segundos

while massa > 0.5: # processo do decaimento
    massa -= massa/2 # a perda 
    time += 50 # adicionando os segundos no temporizador, se decaiu passou 50 segundos

print(f'Massa inicial:{massa_inicial}')
print(f'Massa Final:{massa}')
print(f'Tempo de Decaimento:{((time//60)//60)%60}:{(time//60)%60}:{time%60}')