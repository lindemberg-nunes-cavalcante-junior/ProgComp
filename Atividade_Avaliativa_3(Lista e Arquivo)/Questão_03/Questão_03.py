'''
. (Valor: 15 pontos) Fazer um programa para gerar automaticamente uma lista de dimensão de n
elementos (n deverá ser solicitado ao usuário, positivo e entre 7 e 60, inclusive), cada elemento dessa 
lista será um número aleatório entre 1 e 60 (inclusive) sem repetição. Após a lista ser gerada, as seguintes 
operações deverão ser implementadas:
a) Deverá ser criada uma segunda lista com todas as combinações possíveis. Cada combinação deverá 
ser uma sub-lista. Cada combinação deverá estar ordenada do menor número para o maior; (feito)

b) A lista de números escolhidos deverá ser salva em um arquivo chamado numeros_escolhidos.txt
(salvar no mesmo diretório/pasta em que o programa está salvo). Nesse arquivo os números deverão 
estar em apenas 1 linha. Utilize ; para separar os valores na linha; (feito)

c) A lista de combinações deverá ser salva em um arquivo chamado combinações.txt (salvar no mesmo 
diretório/pasta em que o programa está salvo). Nesse arquivo cada combinação deverá estar em 1 
linha. Utilize ; para separar os valores na linha; (feito)

d) No final deverão ser exibidos na tela quantas combinações foram geradas, e quais as probabilidades
de se acertar a sena, a quina e a quadra. (falta)
'''
import sys,random,os,math

dirarquivo = os.path.abspath(__file__)
dirarquivo = os.path.dirname(dirarquivo)

x = int(input('Digite um número de 7 e 60:'))

if x < 7 or x > 60:
    sys.exit('Digite um número na faixa pedida.')

lista = random.sample(range(1,61), x)
lista.sort()


arqentrada = open(dirarquivo + '\\numeros_escolhidos.txt','w',encoding='utf-8')
for i in lista:
    arqentrada.write(f'{i};')
arqentrada.close()

combos = [[]]
for n in lista:
    combos += [combinar + [n] for combinar in combos]
for x in range(len(combos)):
    combos[x].sort()

salvarN = open(dirarquivo + '\\combinações.txt','w',encoding='utf-8')
contador = 0

for linhas in combos:
    for items in range(len(linhas)):
        salvarN.write(f"{linhas[items]};")
    contador += 1
    salvarN.write(f"\n")
salvarN.close()

print(f'Foram geradas {contador} combinações e a probabilidade de acerta: Quadra = {(math.comb(len(lista),4)*math.comb(54,2))/math.comb(60,6)}, Quina = {(math.comb(len(lista),5)*math.comb(54,1))/math.comb(60,6)}, Sena = {1/math.comb(60,6)}')








'''listaAux = [random.sample(range(1,61), x) for _ in range(60)]
for i in listaAux:
    i.sort()

arqentrada = open(dirarquivo + '\\combinações.txt','w',encoding='utf-8')
for i in listaAux:
    arqentrada.write(f'\n{i};')
arqentrada.close()'''