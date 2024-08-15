'''
Uma família fez uma viagem de carro e quer detalhes sobre o desempenho do veículo. 
Faça um programa que pergunta: o momento inicial da partida (hora e minuto), o momento de chegada 
(hora e minuto), o número de segundos parados para descanso, o número de litros de combustível gasto 
(em l), o preço do litro de combustível (em R$) e a distância percorrida (em Km); 
Após receber os dados, o programa informa dados típicos de um computador de bordo: 
a) o tempo de viagem (em segundos)
b) a velocidade média (Km/h) global e a velocidade média em movimento (Km/h) 
c) o custo da viagem com combustível (em R$)
d) o desempenho do carro (em Km/l, l/h e R$/Km).
'''

T_Inicial = float(input('Informe o tempo de partida(H.M):'))
T_Final = float(input('Informe o tempo de chegada(H.M):'))
Combustivel = float(input('Informe o preço do combustível:(R$)'))
Litro = float(input('Litros de combustível usado:'))
Distancia = float(input('Informe a distância percorrida:'))

if T_Inicial >= 0 and T_Final > 0 and Combustivel > 0 and Litro > 0 and Distancia > 0:
    print('--------------------------------------------------------------------------')
    T_H_inicial = int(round(T_Inicial, 2))
    T_M_inicial = round(T_Inicial - T_H_inicial, 2)
    T_H_Final = int(round(T_Final, 2))
    T_M_Final = round(T_Final - T_H_Final, 2)
    tempo_viagem = ((T_H_Final * 3600) + ((T_M_Final * 10) * 60)) - ((T_H_inicial * 3600) + ((T_M_inicial * 10) * 60))
    print(f'O tempo de viagem é:{tempo_viagem} segundos')

    Vm_global= Distancia/((((T_H_Final * 3600) + ((T_M_Final * 10) * 60))/3600) + (((T_H_inicial * 3600) + ((T_M_inicial * 10) * 60))/3600))
    Vm_movimento = Distancia/(((T_H_Final * 3600) + ((T_M_Final * 10) * 60)) - ((T_H_inicial * 3600) + ((T_M_inicial * 10) * 60))/3600)
    print(f'Velocidade média global: {Vm_global:0.2f} KM/H, velocidade média em movimento: {Vm_movimento:0.2f} KM/H')

    custo = Combustivel * Litro
    print(f'O custo foi: R$ {custo}')
    
    H_viagem = tempo_viagem / 3600
    KM_L =  Distancia/Litro
    L_H = Litro/H_viagem
    R_KM = custo/Distancia
    print(f'Os desempenhos são: {KM_L:0.2f} Km/l, {L_H:0.2f} l/h e {R_KM:0.2f} R$/Km')
    print('--------------------------------------------------------------------------')