'''
Faça um programa que:
a) Solicite ao usuário um nome de uma máquina de destino (HOST); (feito)
b) Em seguida realize o rastreamento e salve a resposta em um arquivo chamado rastreio.txt; (feito)
c) Indique o menor tempo em que cada uma das máquinas no caminho foi atingida. Ignore os tempos 
que não puderam ser determinados, aqueles com pelo menos um * na saída do tracert.
'''
import subprocess,os

dirarquivo = os.path.abspath(__file__)
dirarquivo = os.path.dirname(dirarquivo)

host = input('Fale uma maquina que queira acessar (URL): ')

strCMD = 'tracert -d4 ' + host

'''caminho = subprocess.run (strCMD, capture_output=True).stdout.decode('latin1')

arqentrada = open(dirarquivo + '\\rastreio.txt','w', encoding='utf-8')
arqentrada.writelines(caminho)
arqentrada.close()'''

arqentrada = open(dirarquivo + '\\rastreio.txt','r', encoding='utf-8')
Tempos = list(arqentrada)
menorTempo = list()

for i in Tempos:
    if i != '\n':
        menorTempo.append(i)
menorTempo = list(i[:-1].split('   ') for i in menorTempo if i[-1:] == '\n')
menorTempo = list()
print(menorTempo)
