
import sys

x = int(input('Informe um número de áte 4 dígitos(0 a 9999):'))

if x >= 0 and x <= 9999:
    if x >=0 and x <= 99:
        resultado = (x // 10) + (x % 10)
        print(resultado)
    elif x >= 100 and x <= 999:
        x1 = x // 100
        xA= x % 100
        x2 = xA // 10
        xA = xA % 10
        print(x1 + x2 + xA)
    elif x >= 1000 and x <= 9999:
        x1 = x // 1000
        xA = x % 1000
        x2 = xA // 100
        xA = xA % 100
        x3 = xA // 10
        xA = xA % 10
        print(x1 + x2 + x3 + xA)
    sys.exit()
else:
    print('informe um número válido')
    sys.exit()
