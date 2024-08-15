'''
Desenvolva um código em Python que solicite ao usuário que informe os comprimentos dos três lados de 
um triângulo. Em seguida, verifique se esses comprimentos podem formar um triângulo. Caso afirmativo, 
calcule e informe os valores dos ângulos do triângulo e classifique-o quanto aos lados e aos ângulos.
• Instruções:
(feito)a) Peça ao usuário para inserir os comprimentos dos três lados do triângulo.

(feito)b) Verifique se os comprimentos fornecidos podem formar um triângulo. Caso contrário, informe 
que não é possível formar um triângulo com esses lados.

(feito)c) Se for possível formar um triângulo, calcule os três ângulos do triângulo.

d) Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) e aos ângulos 
(agudo, obtuso ou retângulo).

e) Exiba a classificação do triângulo quanto aos lados e aos ângulos.
• Observações:
(feito)o Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, é necessário 
verificar a seguinte condição: A soma de quaisquer dois lados de um triângulo deve ser 
sempre maior que o terceiro lado.

o Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo.

(feito)o Para classificar quanto aos lados, verifique se os três lados são iguais (equilátero), se dois 
lados são iguais (isósceles) ou se todos os lados são diferentes (escaleno).

o Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 90 graus 
(obtuso), se um dos ângulos é igual a 90 graus (retângulo) ou se todos os ângulos são 
menores que 90 graus (agudo).

o Considere que os ângulos são expressos em graus.
Desenvolva o código em Python para atender às especificações acima
'''
import math
L_1 = float(input('Informe um dos lado:'))
L_2 = float(input('Informe um dos lado:'))
L_3 = float(input('Informe um dos lado:'))

if L_1 + L_2 > L_3 and L_1 + L_3 > L_2 and L_2 + L_3 > L_1:
    if L_1 == L_2 == L_3:
        tipo = 'equilátero'
    elif L_1 == L_2 != L_3 or L_1 == L_3 != L_2 or L_2 == L_3 != L_1:
        tipo = 'isósceles'
    else:
        tipo = 'escaleno'
    Ang1 = math.degrees(math.acos((math.pow(L_1) + L_2 - L_3)/2))
    if Ang1 > 90 or Ang2 > 90 or Ang3 > 90:
        tipo2 = 'obtuso'
    elif Ang1 == 90 or Ang2 == 90 or Ang3 == 90:
        tipo2 = 'retângulo'
    elif Ang1 < 90 and Ang2 < 90 and Ang3 < 90:
        tipo2 = 'agudo'
    print(f"Seu triângulo pelos lados é {tipo} e pelos ângulos é {tipo2}")
else:
    print("Impossível formar um triangulo com esses lados.")
'''
Ang1 = round(math.degrees(math.acos((L_1 * L_1 + L_2 * L_2 - L_3 * L_3)/(2 * L_1 *L_2))), 2)
Ang2 = round(math.degrees(math.acos((L_3 * L_3 + L_2 * L_2 - L_1 * L_1)/(2 * L_3 *L_2))), 2)
Ang3 = round(math.degrees(math.acos((L_3 * L_3 + L_1 * L_1 - L_2 * L_2)/(2 * L_3 *L_1))),2)
'''

