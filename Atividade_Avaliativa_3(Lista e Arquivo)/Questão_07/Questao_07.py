'''
7. (Valor: 15 pontos) A partir do arquivo alunos_ifrn.csv, fazer um programa que:
a) Montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista 
deverá ser a sigla do campus e a segunda a quantidade de alunos daquele campus, no final deverá 
adicionada a cada sub-lista o percentual correspondente de alunos do campus em relação ao total de 
alunos do IFRN (limitar a 2 casas decimais). Essa lista deverá ser salva em um arquivo chamado 
alunos_ifrn_campus.csv (esse arquivo deverá ser salvo no mesmo diretório/pasta do programa). 
onde cada linha deverá ser os dados de cada sub-lista separados por ;;(feita)

b) Montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista 
deverá ser o ano de ingresso do aluno e a segunda posição a quantidade de alunos que ingressaram 
naquele ano. Essa lista deverá ser salva em um arquivo chamado alunos_ifrn_ano.csv (esse arquivo 
deverá ser salvo no mesmo diretório/pasta do programa). onde cada linha deverá ser os dados de 
cada sub-lista separados por ;; (lista feita)

c) Liste os campus, peça ao usuário para escolher um e montar uma segunda lista onde cada posição 
deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser o nome do curso e a 
segunda posição deverá ser quantidade de alunos daquele curso naquele campus. Essa lista deverá 
ser salva em um arquivo chamado alunos_ifrn_campus_curso.csv (esse arquivo deverá ser salvo 
no mesmo diretório/pasta do programa). onde cada linha deverá ser os dados de cada sub-lista 
separados por ;;
'''
import os

direntrada = os.path.abspath(__file__)
direntrada = os.path.dirname(direntrada)

arqentrada = open(direntrada + '\\alunos_ifrn.csv','r',encoding='utf-8')

titulo = arqentrada.readline()
listaentrada = [i[:-1].split(';') for i in arqentrada if i[-1:] =='\n' ]
arqentrada.close()

# Referente a letra A
listaCampus = list(map(lambda x: x[len(x)-1],listaentrada)) # Pegar apenas os campos
listaSigla = list()

for i in listaCampus: # pegar as siglas, mas não repetir elas.
    if i not in listaSigla:
        listaSigla.append(i)

listaCampusAlunos = list(map(lambda x: [x, listaCampus.count(x)],listaSigla))
AlunosTotais = sum(list(map(lambda x: x[1],listaCampusAlunos)))
CampusPorcentagem = list(map(lambda x: [x[0], x[1], round(((x[1]/AlunosTotais) * 100), 2)],listaCampusAlunos))

arqentrada = open(direntrada + '\\alunos_ifrn_campus.csv','w', encoding='utf-8')
for i in CampusPorcentagem:
    arqentrada.write(f'{i[0]};{i[1]};{i[2]}\n')
arqentrada.close()

# Referente a letra B
AlunosAno = list(map(lambda x: x[7][0:4],listaentrada))
AnosQuantidade = list()

for i in AlunosAno:
    if i not in AnosQuantidade:
        AnosQuantidade.append(i)
AlunosAno = list(map(lambda x: [x, AlunosAno.count(x)],AnosQuantidade))

arqentrada = open(direntrada + '\\alunos_ifrn_ano.csv','w', encoding='utf-8')
for i in AlunosAno:
    arqentrada.write(f'{i[0]};{i[1]}\n')
arqentrada.close()

# Referente a letra C
print(f'Os campus disponíveis são: {listaSigla}')
campus = input('Escolha um Campus: ')

listaCursos = list()

for i in listaentrada:
    if campus in i:
        listaCursos.append(i)
listaCursos = list(map(lambda x: x[5],listaCursos))
listaCursos = list(map(lambda x: [x, listaCursos.count(x)], listaCursos)) # Separando o curso com suas quantidades de alunos

arqentrada = open(direntrada + '\\alunos_ifrn_campus_curso.csv','w', encoding='utf-8')
for i in listaCursos:
    arqentrada.write(f'{i[0]};{i[1]}\n')
arqentrada.close()



