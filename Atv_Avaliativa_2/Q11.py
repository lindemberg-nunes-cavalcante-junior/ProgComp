'''
11. (Valor: 15 pontos) Um robô pode se mover em oito sentidos em um plano cartesiano: U (cima); D (baixo); 
R (direita); L (esquerda); O (noroeste/cima-esquerda); N (nordeste/cima-direita); E (sudeste/baixo-direita) 
e W (sudoeste/baixo-esquerda).
Faça um programa que:
a) Solicite ao usuário a posição inicial do robô (suas coordenadas X e Y);
b) Solicite ao usuário uma string. Letras maiúsculas e minúsculas são indistintas e aquelas 
informadas que estejam fora das estabelecidas (U, D, R, L, O, N, E e W) devem ser ignoradas.
c) Com base em cada letra válida (U, D, R, L, O, N, E e W), o robô deverá se deslocar 1 (uma) 
unidade em cada eixo (X e Y) por vez em função da direção;
Ao final, indique:
a) a posição inicial do robô (coordenadas X e Y);
b) a posição final do robô (coordenadas X e Y);
c) quantos movimentos válidos ele executou;
d) quais foram os movimentos válidos que ele executou;
e) em que quadrante ele iniciou (posição inicial de X e Y) e;
f) em que quadrante ele terminou (posição final de X e Y)
'''

x1 = int(input('Informe o X do seu robô:'))
x2 = x1
y1 = int(input('Informe o Y do seu robô:'))
y2 = y1
string = input('Agora informe uma série de letras qualquer:').upper()

movimentos = 'UDRLONEW'
valido = 0
Qinicial = 0
Qfinal = 0

if  x1 > 0 and y1 > 0:
    Qinicial = 1
elif x1 < 0 and y1 > 0:
    Qinicial = 2
elif x1 < 0 and y1 < 0:
    Qinicial = 3
elif x1 > 0 and y1 < 0:
    Qinicial = 4

for i in string:
    if i == 'U': 
        y2 += 1
        valido += 1
    elif i == 'D': 
        y2 -= 1
        valido += 1
    elif i == 'R': 
        x2 += 1
        valido += 1
    elif i == 'L':
        x2 -= 1
        valido += 1
    elif i == 'O': 
        y2 += 1 
        x2 -= 1
        valido += 1
    elif i == 'N':
        y2 += 1
        x2 += 1
        valido += 1
    elif i == 'E':
        y2 -= 1
        x2 += 1
        valido += 1
    elif i == 'W':
        y2 -= 1
        x2 -= 1
        valido += 1

if  x2 > 0 and y2 > 0:
    Qfinal = 1
elif x2 < 0 and y2 > 0:
    Qfinal = 2
elif x2 < 0 and y2 < 0:
    Qfinal = 3
elif x2 > 0 and y2 < 0:
    Qfinal = 4

print(f'Seu robô foi de ({x1},{y1}) para ({x2},{y2})')
print(f'Foi do Quadrante {Qinicial} para o Quadrante {Qfinal}')
print(f'Seu movimentos válidos foram {valido} e são:', end='')
for i in string:
    for a in movimentos:
        if  i == a: print(f'{i}', end=',')
    


