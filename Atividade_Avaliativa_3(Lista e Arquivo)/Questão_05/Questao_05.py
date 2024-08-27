'''
5. (Valor: 15 pontos) Utilizando as listas abaixo... 
gabarito = ['A', 'C', 'B', 'A', 'E', 'D', 'D', 'C', 'A', 'A'] 
lista_alunos = [ ['Aluno 01', 'B', 'D', 'E', 'E', 'C', 'D', 'A', 'B', 'C', 'D'], 
['Aluno 02', 'C', 'D', 'A', 'B', 'D', 'A', 'A', 'C', 'B', 'E'], 
['Aluno 03', 'A', 'A', 'B', 'D', 'C', 'E', 'E', 'A', 'A', 'C'], 
['Aluno 04', 'B', 'B', 'C', 'C', 'D', 'E', 'D', 'D', 'E', 'E'], 
['Aluno 05', 'B', 'B', 'D', 'A', 'A', 'E', 'B', 'D', 'E', 'C'], 
['Aluno 06', 'C', 'C', 'D', 'E', 'B', 'B', 'C', 'D', 'E', 'A'], 
['Aluno 07', 'B', 'A', 'A', 'B', 'B', 'C', 'D', 'E', 'A', 'B'], 
['Aluno 08', 'D', 'E', 'A', 'B', 'B', 'C', 'C', 'D', 'A', 'A'], 
['Aluno 09', 'A', 'A', 'A', 'C', 'B', 'D', 'D', 'E', 'D', 'C'],] 
['Aluno 10', 'B', 'B', 'D', 'E', 'C', 'D', 'C', 'E', 'B', 'A'] ] 
Fazer um programa que realize as seguintes orientações:  
a) O programa deverá adicionar no final de cada sub-lista do item (b) a quantidade de acertos do aluno; (feito)
b) A lista deverá ser ordenada pela quantidade de acertos de forma decrescente; (feito)
c) O programa deverá exibir no final o gabarito e os nomes de cada aluno, as opções que cada um 
marcou e a nota obtida. 
'''
gabarito = ['A', 'C', 'B', 'A', 'E', 'D', 'D', 'C', 'A', 'A'] 
lista_alunos = [
    ['Aluno 01', 'B', 'D', 'E', 'E', 'C', 'D', 'A', 'B', 'C', 'D'], 
    ['Aluno 02', 'C', 'D', 'A', 'B', 'D', 'A', 'A', 'C', 'B', 'E'], 
    ['Aluno 03', 'A', 'A', 'B', 'D', 'C', 'E', 'E', 'A', 'A', 'C'], 
    ['Aluno 04', 'B', 'B', 'C', 'C', 'D', 'E', 'D', 'D', 'E', 'E'], 
    ['Aluno 05', 'B', 'B', 'D', 'A', 'A', 'E', 'B', 'D', 'E', 'C'], 
    ['Aluno 06', 'C', 'C', 'D', 'E', 'B', 'B', 'C', 'D', 'E', 'A'], 
    ['Aluno 07', 'B', 'A', 'A', 'B', 'B', 'C', 'D', 'E', 'A', 'B'], 
    ['Aluno 08', 'D', 'E', 'A', 'B', 'B', 'C', 'C', 'D', 'A', 'A'], 
    ['Aluno 09', 'A', 'A', 'A', 'C', 'B', 'D', 'D', 'E', 'D', 'C'],
    ['Aluno 10', 'B', 'B', 'D', 'E', 'C', 'D', 'C', 'E', 'B', 'A'] ]

acertos = 0
pontuacao = list([x[0]] for x in lista_alunos)

for i in range(len(lista_alunos)):
    listaAux = list([x[i] for i in range(1,len(lista_alunos ) + 1)] for x in lista_alunos)
    for x in range(len(gabarito)):
        if listaAux[i][x] == gabarito[x]:
            acertos += 1
            print(acertos)
    pontuacao[i].append(acertos)
    acertos = 0
pontuacao.sort(key=lambda x: x[1],  reverse=True)

print(f'O gabarito é: {gabarito}')
for i in range(len(pontuacao)):
    listaAux = list([x[i] for i in range(1,len(lista_alunos ) + 1)] for x in lista_alunos)
    for x in pontuacao:
        print(f'O {x[0]} obteve {x[1]} suas repostas foram: {listaAux[i]}')